#!/usr/bin/python3

"""function that writes a stirng to text file"""


def write_file(filename="", text=""):
    """returns the number of characters written to file"""
    with open(filename, "w") as f:
        return f.write(text)
