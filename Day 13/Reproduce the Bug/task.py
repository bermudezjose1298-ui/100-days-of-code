from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
#The randint can select a number out of range, this is due that when it reaches the index 6, that is a value out of range, since arrays starts with a 0 so in this case, the range would be 0~5,
#so the number 0 does not get print and the number 6 generates an error, to fix this, we subtract 1 from the int so is always in scope, or can just modify the scope to 0~5
dice_num = randint(0, 5)
print(dice_images[dice_num])
