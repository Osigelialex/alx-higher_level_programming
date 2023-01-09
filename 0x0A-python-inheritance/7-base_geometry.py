#!/usr/bin/python3

"""
Defines a geometry class
"""


class BaseGeometry:
    """
    implementing class
    """

    """
    method to calculate area
    """

    def area(self):
        """
        raises an exception
        """
        raise Exception("area() is not implemented")

    """
    Integer validator function
    """

    def integer_validator(self, name, value):
        """
        validates an integer value
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
