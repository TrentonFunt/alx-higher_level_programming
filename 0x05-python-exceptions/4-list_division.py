#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            # Extract elements from the lists
            num1 = my_list_1[i] if i < len(my_list_1) else 0
            num2 = my_list_2[i] if i < len(my_list_2) else 0

            # Perform division, handle exceptions
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("division by 0")
                result = 0
            except (TypeError, ValueError):
                print("wrong type")
                result = 0

            # Append the result to the new list
            result_list.append(result)

    except IndexError:
        # Handle if either my_list_1 or my_list_2 is too short
        print("out of range")

    finally:
        # Return the new list
        return result_list
