import sqlite3
from flask import Flask, request, render_template_string, redirect
import datetime
import os

DB = "piso_wifi.db"

# ----------------------- DATABASE SETUP -----------------------

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS vouchers(
            code TEXT PRIMARY KEY,
            minutes INTEGER,
            used INTEGER DEFAULT 0
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS sessions(
            user_ip TEXT PRIMARY KEY,
            voucher TEXT,
            start_time TEXT,
            end_time TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()


# ----------------------- FLASK APP -----------------------

app = Flask(__name__)


# ----------------------- HTML TEMPLATES -----------------------

login_page = """
<!DOCTYPE html>
<html>
<head>
<title>Piso WiFi Login</title>
<style>
body { font-family: Arial; text-align:center; padding-top:100px; }
input { padding:10px; font-size:18px; }
button { padding:10px 20px; font-size:18px; }
</style>
</head>
<body>
<h1>Piso WiFi</h1>
<p>Enter Voucher Code:</p>
<form method="POST">
    <input name="voucher" placeholder="Voucher Code"/>
    <br><br>
    <button type="submit">Login</button>
</form>
<p style="color:red;">{{ error }}</p>
</body>
</html>
"""

success_page = """
<!DOCTYPE html>
<html>
<head>
<title>Piso WiFi</title>
</head>
<body style="font-family:Arial; text-align:center; padding-top:100px;">
<h1>Login Successful!</h1>
<p>Time remaining: <b>{{ mins }} minutes</b></p>
<p>Your internet is now active.</p>
</body>
</html>
"""

expired_page = """
<!DOCTYPE html>
<html>
<head>
<title>Expired</title>
</head>
<body style="font-family:Arial; text-align:center; padding-top:100px;">
<h1>Session Expired</h1>
<p>Your time is up.</p>
</body>
</html>
"""

# ----------------------- HELPER FUNCTIONS -----------------------

def get_client_ip():
    return request.remote_addr

def add_minutes(minutes):
    return datetime.datetime.now() + datetime.timedelta(minutes=minutes)

def get_session(ip):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM sessions WHERE user_ip = ?", (ip,))
    row = c.fetchone()
    conn.close()
    return row

def time_left(end_time):
    now = datetime.datetime.now()
    end = datetime.datetime.fromisoformat(end_time)
    remaining = end - now
    return max(0, int(remaining.total_seconds() / 60))


# ----------------------- ROUTES -----------------------

@app.route("/", methods=["GET", "POST"])
def login():
    ip = get_client_ip()

    # check if user already has an active session
    active = get_session(ip)
    if active:
        mins = time_left(active[3])
        if mins > 0:
            return render_template_string(success_page, mins=mins)
        else:
            return render_template_string(expired_page)

    error = ""

    if request.method == "POST":
        code = request.form["voucher"].strip().upper()

        conn = sqlite3.connect(DB)
        c = conn.cursor()
        c.execute("SELECT * FROM vouchers WHERE code=?", (code,))
        voucher = c.fetchone()

        if not voucher:
            error = "Invalid voucher code."
        elif voucher[2] == 1:
            error = "Voucher already used."
        else:
            # mark voucher used
            c.execute("UPDATE vouchers SET used=1 WHERE code=?", (code,))

            # create session
            minutes = voucher[1]
            start = datetime.datetime.now().isoformat()
            end = add_minutes(minutes).isoformat()

            c.execute(
                "INSERT OR REPLACE INTO sessions(user_ip, voucher, start_time, end_time) VALUES (?, ?, ?, ?)",
                (ip, code, start, end)
            )
            conn.commit()
            conn.close()

            return render_template_string(success_page, mins=minutes)

        conn.close()

    return render_template_string(login_page, error=error)


# ----------------------- ADMIN: CREATE VOUCHERS -----------------------

@app.route("/create/<code>/<int:minutes>")
def create_voucher(code, minutes):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    try:
        c.execute("INSERT INTO vouchers(code, minutes) VALUES(?,?)", (code.upper(), minutes))
        conn.commit()
        msg = f"Voucher {code} created: {minutes} minutes"
    except:
        msg = "Voucher already exists."
    conn.close()
    return msg


# ----------------------- RUN APP -----------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
