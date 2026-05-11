weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi <18.5:
    print("You are underweight")
elif bmi <= 24.9:
    print("You are normal")
else:
    print("You are overweight")