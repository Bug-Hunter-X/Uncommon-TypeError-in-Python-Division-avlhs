def function_with_uncommon_error_fixed(a, b):
    try:
        # Explicit type conversion for safe division
        b = int(b)
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except (ValueError, TypeError) as e:
        return f"Error: Invalid input type: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage with corrected input handling
result = function_with_uncommon_error_fixed(10, '2')
print(result)  # Output: 5.0

result = function_with_uncommon_error_fixed(10, 0)
print(result)  # Output: Error: Division by zero

result = function_with_uncommon_error_fixed(10, 'abc')
print(result) # Output: Error: Invalid input type: invalid literal for int() with base 10: 'abc'