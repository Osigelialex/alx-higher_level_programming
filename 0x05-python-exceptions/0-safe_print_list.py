#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        number = ""
        for element in range(x):
            number += str(my_list[element])
        return int(number)
    except IndexError:
        number = ""
        for element in my_list:
            number += str(element)
        return int(number)
