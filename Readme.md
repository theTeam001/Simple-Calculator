# Simple Command-Line Calculator

A simple command-line calculator that performs basic arithmetic operations like addition, subtraction, multiplication, division, and additional functionalities such as square root, exponentiation, and viewing history of calculations. The project is structured into multiple Python modules to demonstrate modular programming and code organization.

## Project Structure

This project is divided into the following Python files:

```
simple-calculator/
│
├── operations.py         # Contains arithmetic operation functions
├── calculator.py         # Contains the calculator logic with user interaction
├── utils.py              # Utility functions for input validation
├── main.py               # Entry point to run the calculator
```

### Modules Description:

- **`operations.py`**: This module contains functions to perform arithmetic operations like addition, subtraction, multiplication, division, and other advanced operations such as square root, exponentiation, and logarithms.
- **`calculator.py`**: This module handles user interaction, prompting the user for input, performing operations, and displaying results. It supports basic arithmetic, square roots, exponentiation, viewing calculation history, and clearing history.
- **`utils.py`**: Contains utility functions such as input validation for ensuring only valid numerical inputs, handling retries, and restricting to positive numbers if required.
- **`main.py`**: The entry point of the program that runs the `calculator()` function from `calculator.py` to start the program.

## Features

- Performs four basic arithmetic operations: **addition**, **subtraction**, **multiplication**, and **division**.
- Supports **square root** and **exponentiation** operations.
- Allows the user to **view calculation history** and **clear history**.
- Handles errors like invalid operator input, division by zero, and invalid number input.
- Allows the user to perform multiple calculations in a session.

## Requirements

- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-calculator.git
   cd simple-calculator
   ```

2. The project doesn't require any external dependencies, so no additional installation steps are needed.

## Usage

1. To start the calculator, run the `main.py` file in your terminal or command prompt:
   ```bash
   python main.py
   ```

2. You will be prompted to choose an operation. The available operations are:
   - Basic arithmetic: **+, -, *, /**
   - Advanced operations: **sqrt** (square root), **pow** (exponentiation)
   - **history** to view the calculation history
   - **clear** to reset the history

3. The calculator will display the result and ask if you want to perform another calculation. Type `y` for yes or `n` to exit the program.

### Example Interaction:
```
Simple Calculator
Enter operation (+, -, *, /, sqrt, pow, history, clear): +
Enter first number: 10
Enter second number: 5
Result: 15.0
Do you want to perform another calculation? (y/n): y

Enter operation (+, -, *, /, sqrt, pow, history, clear): sqrt
Enter the number to find the square root of: 16
Result: 4.0
Do you want to perform another calculation? (y/n): y

Enter operation (+, -, *, /, sqrt, pow, history, clear): history
Calculation History:
1. 10.0 + 5.0 = 15.0
2. sqrt(16.0) = 4.0
Do you want to perform another calculation? (y/n): n
```

## How It Works

1. **`operations.py`** defines basic functions for each arithmetic operation:
   - `add(x, y)`
   - `subtract(x, y)`
   - `multiply(x, y)`
   - `divide(x, y)`
   - `sqrt(x)` for square root
   - `power(x, y)` for exponentiation (`x ^ y`)

2. **`calculator.py`** manages the user input, prompts for the numbers and operator, invokes functions from `operations.py`, and displays the result. It also tracks the calculation history and allows for history viewing and clearing.

3. **`utils.py`** provides helper functions, such as validating that the user's input is a valid number and handling retries if the input is incorrect.

4. **`main.py`** is the entry point for the program. It calls the `calculator()` function to start the interactive calculator.

## Error Handling

- The calculator handles **division by zero** and raises an appropriate error message when this happens.
- **Invalid input** (such as entering non-numeric values for numbers or invalid operators) is caught and the user is prompted to try again.
- If the user tries to calculate the square root of a negative number or enters an invalid base or exponent, appropriate error messages are displayed.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contributing

Feel free to submit issues, bugs, or pull requests. Contributions are always welcome!
