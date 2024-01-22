#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    output = []

    for i in range(list_length):
        try:
            # Check for IndexError first
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError("out of range")

            # Check for ZeroDivisionError
            if my_list_2[i] == 0:
                raise ZeroDivisionError("division by 0")

            # Check for TypeError
            if not isinstance(my_list_1[i],
                              (int, float)) or not isinstance(my_list_2[i],
                                                              (int, float)):
                raise TypeError("wrong type")

            result = my_list_1[i] / my_list_2[i]

        except ZeroDivisionError as e:
            print(e)
            result = 0

        except (TypeError, IndexError) as e:
            print(e)
            result = 0

        finally:
            output.append(result)

    return output
