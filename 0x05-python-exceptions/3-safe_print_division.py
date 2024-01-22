#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        # Attempt to perform the division
        result = a / b
    except ZeroDivisionError:
        # Handle division by zero
        result = None
    except Exception:
        # Handle other exceptions
        result = None
    finally:
        # Print the result in the finally block without additional formatting
        print("Inside result: {}".format(result))

    return result
