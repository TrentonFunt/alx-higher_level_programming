#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix to store value
    result_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Create a new row for the new  matrix
        squared_row = [x ** 2 for x in row]
        # Append the squared row to the result matrix
        result_matrix.append(squared_row)

    return result_matrix
