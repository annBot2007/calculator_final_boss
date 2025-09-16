# Intermediate Calculator

# Takes two numbers as input and adds, subtracts, multiplies or divides them based on user input

# Uses a loop to keep calculating without restarting the program
# Error handling (dividing by 0, not giving a number as input, etc.)
# Add exponentiation and modulus

# The mathematical functions:
def add(num1, num2): return num1 + num2

def subtract(num1, num2): return num1 - num2

def multiply(num1, num2): return num1 * num2

def divide(num1, num2): return num1 / num2

def exponent(num1, num2): return num1 ** num2

def modulo(num1, num2): return num1 % num2

# Dictionary of operators that we'll be working with:

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "e": exponent,
    "%": modulo,
}

# Calculator logic:

while True:
    # Taking first number, second number and operator as inputs from the user

    try:
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")
        operator = input("Enter operator (+, -, *, /, e, %): ")

        if operator in operators:
            try:
                result = operators[operator](num1, num2)
                print(result)
            except ZeroDivisionError:
                print("Division by zero is not possible.")
        else:
            print("Invalid operator.")

    except ValueError:
        print("Enter only numbers.")

    # Making the loop run multiple times till

    should_continue = input("\nDo you want to continue? (y/n): ")

    if should_continue != "y":
        print("Exiting Program...")
        break
