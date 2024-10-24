def safe_divide(numerator, denominator):
    """Perform division with error handling for zero and non-numeric inputs."""
    try:
        # Convert inputs to float
        num = float(numerator)
        denom = float(denominator)
        
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
