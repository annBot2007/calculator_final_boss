# Slightly Advanced Calculator

# Takes two numbers as input and adds, subtracts, multiplies or divides them based on user input

# Uses a loop to keep calculating without restarting the program
# Error handling (dividing by 0, not giving a number as input, etc.)
# Add exponentiation and modulus

# Support multiple operations like 2 * 3 + 5
# Memory feature to use the previous number in further calculations
# Add history of calculations to list all past results if asked

# Calculator logic:

past_calculations = []
last_result = None

while True:
    # Instead of using taking the operators and operands separately, we can use the Python eval() method
    # This optimizes the code a lot, long live the eval() method

    option_choice = input("\nWhat would you like to do?"
                          "\n1: Calculation"
                          "\n2: List all previous calculations"
                          "\n3: Exit"
                          "\nEnter your choice: ")

    if option_choice == "1":
        try:
            expression = input("\nEnter a mathematical expression (use 'ans' for last result): ")

            if last_result is not None:
                expression = expression.replace("ans", str(last_result))

            result = eval(expression)

            last_result = result
            past_calculations.append(f"{expression} = {result}")

            print(f"\n{expression} = {result}")
        except ValueError:
            print("Enter only numbers.")
        except ZeroDivisionError:
            print("Division by zero is not possible.")
        except NameError:
            print("Name error.")

    elif option_choice == "2":
        print("\nPrevious calculations: ")
        for calc in past_calculations:
            print(calc)

    elif option_choice == "3":
        print("\nExiting Program...")
        break

    else:
        print("Invalid input")
