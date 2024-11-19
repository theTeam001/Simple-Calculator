# utils.py

def validate_number_input(input_string, positive_only=False, retry_limit=3):
    """
    Validates the user's input as a valid number.

    Parameters:
    - input_string (str): The input string to validate.
    - positive_only (bool): If True, only accepts positive numbers.
    - retry_limit (int): The number of retry attempts allowed before raising an error.

    Returns:
    - float: The validated number.
    
    Raises:
    - ValueError: If the input is not a valid number or doesn't meet the conditions.
    """
    retries = 0
    
    while retries < retry_limit:
        try:
            # Attempt to convert the input to a float
            number = float(input_string)
            
            # If positive_only is True, check if the number is positive
            if positive_only and number <= 0:
                raise ValueError("Please enter a positive number.")
            
            return number
        
        except ValueError as e:
            retries += 1
            # Provide feedback to the user
            if retries < retry_limit:
                input_string = input(f"Invalid input. {e} You have {retry_limit - retries} attempt(s) left. Try again: ")
            else:
                raise ValueError(f"Invalid input. {e} You have exceeded the maximum retry attempts.")
    
    # If maximum retries are exceeded, raise an exception
    raise ValueError("Maximum retry attempts exceeded. Please try again later.")
