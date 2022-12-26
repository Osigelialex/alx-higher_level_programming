#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Initializes the squre"""

    def __init__(self, size):
        self.size = size

    """Calculates the area of the square"""

    def area():
        return self.__size ** 2

    """gets the value"""

    def size(self):
        return self.__size

    """sets the size"""

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """prints in stdout the square"""

    def my_print(self):
        width = self.size

        if width == 0:
            print()

        for i in range(width):
            for j in range(width):
                print("#", end="")
            print()
