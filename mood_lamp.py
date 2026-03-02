import turtle

screen = turtle.Screen()
screen.title("AI Mood Lamp")

print("How are you feeling today?")
mood = input("Type your mood: ").lower()

if "happy" in mood or "excited" in mood:
    screen.bgcolor("yellow")
    message = "Yay! Stay happy 😄"

elif "sad" in mood or "tired" in mood:
    screen.bgcolor("blue")
    message = "It's okay. Rest muna 💙"

elif "angry" in mood or "mad" in mood:
    screen.bgcolor("red")
    message = "Take a deep breath ❤️"

elif "calm" in mood or "relaxed" in mood:
    screen.bgcolor("green")
    message = "Keep the peaceful vibes 🌿"

else:
    screen.bgcolor("purple")
    message = "You're unique ✨"

pen = turtle.Turtle()
pen.hideturtle()
pen.color("white")
pen.penup()
pen.goto(0, 0)
pen.write(message, align="center", font=("Arial", 24, "bold"))

turtle.done()
