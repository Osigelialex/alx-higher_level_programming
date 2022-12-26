#!/usr/bin/python3
"""Defines a Square"""


class Square:
    """Initializes the squre"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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
        spaceX = " " * self.position[0]
        spaceY = "\n" * self.position[1]

        if width == 0:
            print()

        print(spaceY)
        for i in range(width):
            print(spaceX, end="")
            for j in range(width):
                print("#", end="")
            print()
