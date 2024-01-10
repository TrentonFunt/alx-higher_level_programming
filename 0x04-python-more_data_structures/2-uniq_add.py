#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create an empty set to store unique integers
    uniq_set = set()

    # Iterate through each element in the list
    for element in my_list:
        # Add the element to the set
        uniq_set.add(element)

    # Sum the unique elements in the set
    result = sum(uniq_set)

    return result
