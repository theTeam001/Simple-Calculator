# calculator.py

from operations import add, subtract, multiply, divide

def calculator():
    print("Simple Calculator")

    while True:
        # Get user input for the operation
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            # Perform the operation based on the input
            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                print("Invalid operator!")
                continue

            print(f"Result: {result}")
            
            # Ask if user wants to perform another calculation
            next_calculation = input("Do you want to perform another calculation? (y/n): ")
            if next_calculation.lower() != "y":
                break

        except ValueError as e:
            print(f"Error: {e}")
