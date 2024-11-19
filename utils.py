# utils.py

def validate_number_input(input_string):
    try:
        return float(input_string)
    except ValueError:
        raise ValueError("Please enter a valid number.")
