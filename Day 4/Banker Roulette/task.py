import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# 1st option, go trough the list and select one of the options with an if
person_to_choose = random.randint(0, len(friends)-1)
print(friends[person_to_choose])

# 2 Option
print(random.choice(friends))
