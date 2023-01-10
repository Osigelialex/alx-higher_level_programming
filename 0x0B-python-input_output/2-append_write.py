#!/usr/bin/python3

"""function that appends to file"""


def append_write(filename="", text=""):
    """returns the number of characters appended to file"""
    with open(filename, "a") as f:
        return f.write(text)
