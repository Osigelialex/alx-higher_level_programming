#!/usr/bin/python3
"""Defines a square"""


class Square:
    """validates size of square"""
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """Calculates the area of the square"""
    def area(self):
        return self.__size ** 2
