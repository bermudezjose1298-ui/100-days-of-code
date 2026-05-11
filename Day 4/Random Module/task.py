import random
import my_module


# random_integer = random.randint(1, 100)
# print(random_integer)
# print(my_module.my_favorite_number)

#This generates a random number between 0 - 1 unless modified by multiplying it to a range
random_number_0_to_1 = random.random() * 10


#This generates a random number between 2 ranges
random_float = random.uniform(1,10)

heads_or_tails = random.randint(0,1)
if heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")
