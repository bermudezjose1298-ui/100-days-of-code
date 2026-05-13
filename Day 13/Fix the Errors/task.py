try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have not entered a number. Please try again with a numerical response")
    age = int(input("How old are you?"))

if age > 18:
    print(f"You can drive at age {age}.")
else:
    print("You are not old enough to drive, you need to at least be 18")
