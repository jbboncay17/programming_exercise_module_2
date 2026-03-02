from operator import truediv

print("Insert Card")
pin=int(input("Input Pin:"))
pinz=123
if pin == pinz:
    print("1. Withdraw")
    print("2. Check Balance")
    print("3. Deposit")
else:
    print("INVALID")

# display "1.) Withdraw"
# display "2.) Check Balance"
# display "3.) Deposit"
# input choice
# IF choice = 1 THEN
# input amount
# IF amount <= balance THEN
# balance ← balance - amount
# output "Withdrawal successful"
# ELSE
# output "Insufficient funds"
# ENDIF
# ELSE IF choice = 2 THEN
# output "Your balance is "
#
# , balance
#
# ELSE
# output "Invalid choice"
# ENDIF
# ELSE IF choice = 3 THEN
# input deposit
# balance ← balance + deposit
# ENDIF
# ELSE
# output "Invalid PIN"
# ENDIF
# END