def my_function():
    for i in range(1, 21):
        #The for loop is iterating through a range from 1 to 20, the if is supposed to print once the value of i reaches 20, but in a range function, i never reaches the top range
        #To make the "if" to be reproduced, we will increase the value to 21
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?
