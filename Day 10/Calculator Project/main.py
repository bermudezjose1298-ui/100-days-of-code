import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(art.logo)
    recycle_value = True
    first_number = float(input("Please enter your first number: "))

    while recycle_value:
        for symbol in functions:
            print(symbol)

        operation_symbol = input("Please enter your operation: ")
        second_number = float(input("Please enter your second number: "))
        answer = functions[operation_symbol](first_number, second_number)
        print(f"{first_number} {operation_symbol} {second_number} = {answer}")

        choice = input(f"Type 'y' to continue using {answer}, or type 'n' to start with a new value: ")

        if choice == "y":
            first_number = answer
        else:
            recycle_value = False
            print("\n" * 20)
            calculator()


calculator()