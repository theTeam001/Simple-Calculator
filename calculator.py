# calculator.py

from operations import add, subtract, multiply, divide, modulus, power, sqrt, log, power_of_10
import math

def calculator():
    history = []  # To store the history of calculations
    
    print("Simple Calculator")
    print("You can perform basic operations: +, -, *, /.")
    print("Additional operations: sqrt (square root), pow (exponentiation), modulus, log (logarithm), power_of_10, history (view calculation history), clear (reset the calculator).")
    
    while True:
        try:
            # Get user input for the operation type
            operation = input("Enter operation (+, -, *, /, sqrt, pow, modulus, log, power_of_10, history, clear): ").strip().lower()
            
            if operation == "history":
                # Display calculation history
                print("Calculation History:")
                if history:
                    for idx, entry in enumerate(history, start=1):
                        print(f"{idx}. {entry}")
                else:
                    print("No calculations yet.")
                continue
            
            if operation == "clear":
                # Clear the calculator history and reset
                history.clear()
                print("Calculator history cleared.")
                continue
            
            if operation == "sqrt":
                num = float(input("Enter the number to find the square root of: "))
                if num < 0:
                    print("Error: Cannot calculate square root of a negative number.")
                    continue
                result = sqrt(num)
                history.append(f"sqrt({num}) = {result}")
            
            elif operation == "pow":
                base = float(input("Enter the base number: "))
                exponent = float(input("Enter the exponent: "))
                result = power(base, exponent)
                history.append(f"{base} ^ {exponent} = {result}")
            
            elif operation == "modulus":
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = modulus(num1, num2)
                history.append(f"{num1} % {num2} = {result}")
            
            elif operation == "log":
                num = float(input("Enter the number for logarithm: "))
                base = float(input("Enter the base for logarithm (default is 10): ") or 10)
                result = log(num, base)
                history.append(f"log({num}, {base}) = {result}")
            
            elif operation == "power_of_10":
                exponent = float(input("Enter the exponent: "))
                result = power_of_10(exponent)
                history.append(f"10 ^ {exponent} = {result}")
            
            else:
                # Get user input for the first number, operator, and second number
                num1 = float(input("Enter first number: "))
                operator = operation
                num2 = float(input("Enter second number: "))

                # Check if the operator is valid and perform the corresponding operation
                if operator == "+":
                    result = add(num1, num2)
                elif operator == "-":
                    result = subtract(num1, num2)
                elif operator == "*":
                    result = multiply(num1, num2)
                elif operator == "/":
                    # Handle division by zero
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                        continue
                    result = divide(num1, num2)
                else:
                    print("Invalid operator! Please choose from (+, -, *, /, sqrt, pow, modulus, log, power_of_10).")
                    continue
                
                history.append(f"{num1} {operator} {num2} = {result}")
            
            # Display the result of the operation
            print(f"Result: {result}")
            
            # Ask if the user wants to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (y/n): ").strip().lower()
            if next_calculation != "y":
                print("Thank you for using the calculator. Goodbye!")
                break

        except ValueError:
            # Handle invalid number input
            print("Error: Invalid input. Please enter a valid number.")
