#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """
    A class representing BaseGeometry.

    Public instance method:
        area(self): Raises an Exception with
        the message 'area() is not implemented.'
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented.'
        """
        raise Exception("area() is not implemented")
