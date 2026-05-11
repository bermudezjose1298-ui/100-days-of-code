programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",

}

groceries_dictionary = {
    "Apple": 3.99,
    "Pear": 4.59,
    "Banana": 3.99,
    "Grape": 3.99
}

#Print all the keys in a dictionary
# for key in groceries_dictionary:
#     print(key)
#
# for value in groceries_dictionary:
#     print(groceries_dictionary[value])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]

    if score >= 91:
        student_grades[student] = 'Outstanding'
    elif score >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif score >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

print(student_grades)

