#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """
    A class representing BaseGeometry.

    Public instance methods:
        area(self): Raises an Exception with the message
        'area() is not implemented.'
        integer_validator(self, name, value):
        Validates the value and raises exceptions if necessary.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented.'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value and raises exceptions if necessary.

        Args:
            name: A string representing the name of the value.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
