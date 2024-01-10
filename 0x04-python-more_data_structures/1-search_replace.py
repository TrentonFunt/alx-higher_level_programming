#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list to store the replaced elements
    new_list = []

    # Iterate through each element in the original list
    for element in my_list:
        # Replace the element if it matches the search value
        new_element = replace if element == search else element
        # Append the modified element to the new list
        new_list.append(new_element)

    return new_list
