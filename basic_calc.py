# Basic Calculator

# Takes two numbers as input and adds, subtracts, multiplies or divides them based on user input

# The mathematical functions:

def add(num1, num2):
    return int(num1) + int(num2)

def subtract(num1, num2):
    return int(num1) - int(num2)

def multiply(num1, num2):
    return int(num1) * int(num2)

def divide(num1, num2):
    return int(num1) / int(num2)

# Taking first number, second number and operator as inputs from the user

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operator = input("Enter operator (+, -, *, /): ")

# if, elif, else to perform and print the function

if operator == "+":
    print(add(num1, num2))
elif operator == "-":
    print(subtract(num1, num2))
elif operator == "*":
    print(multiply(num1, num2))
elif operator == "/":
    print(divide(num1, num2))
else:
    print("Invalid operator")
