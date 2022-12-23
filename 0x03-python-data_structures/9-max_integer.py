#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_value = my_list[0]
    for i in my_list:
        if i > max_value:
            max_value = i
    return max_value
