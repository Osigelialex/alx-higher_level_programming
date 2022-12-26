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

    @property
    def size(self):
        return self.__size

    """sets the size"""

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """gets position value"""

    @property
    def position(self):
        return self.__position

    """sets position value"""

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
