#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    for i in range(list_length):
        try:
            # Try to divide elements of the lists
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 1  # Avoid division by 0
            division_result = element_1 / element_2
            result_list.append(division_result)

        except ZeroDivisionError:
            # Handle division by 0
            print("division by 0")
            result_list.append(0)

        except (TypeError, ValueError):
            # Handle wrong type
            print("wrong type")
            result_list.append(0)

        except IndexError:
            # Handle out of range
            break  # Break out of the loop when IndexError occurs

        finally:
            # Cleanup or final statements (if any)
            pass

    else:
        # This block will be executed if the loop completes
        print("out of range")

    return result_list
