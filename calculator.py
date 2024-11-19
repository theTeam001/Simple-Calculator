# calculator.py

from operations import add, subtract, multiply, divide

def calculator():
    print("Simple Calculator")
    print("You can perform basic operations: +, -, *, /.")
    
    while True:
        try:
            # Get user input for the first number, operator, and second number
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
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
                print("Invalid operator! Please choose from (+, -, *, /).")
                continue

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