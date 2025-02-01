def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input type"
except Exception as e:
        return f"An unexpected error occurred: {e}"

# Example usage with a tricky type error
result = function_with_uncommon_error(10, '2')
print(result)  # Output: Error: Invalid input type