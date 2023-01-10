#!/usr/bin/python3

"""function to read file"""


def read_file(filename=""):
    """filename: name of file"""
    with open(filename, encoding="utf-8") as a_file:
        data = a_file.read()
        print(data, end="")
