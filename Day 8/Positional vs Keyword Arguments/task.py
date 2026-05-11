# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")



#function with multiple inputs
def greet_with_location(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}?")

#positional parameters
#greet_with_location("John", "Oaxaca")

#keyword parameters
#greet_with_location(location="New York", name="John")


def calculate_love_score(name1, name2):
    value1 = 0
    value2 = 0

    validation_text = name1 + name2
    for letter in validation_text.lower():
        if letter == "t" or letter == "r" or letter == "u" or letter == "e":
            value1 += 1
        if letter == "l" or letter == "o" or letter == "v" or letter == "e":
            value2 += 1

    print(f"{value1}{value2}")


calculate_love_score(name1="Angela Yu", name2="Jack Bauer")
