#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for i in my_list:
        if my_list.index(i) == idx:
            new_list.append(element)
        else:
            new_list.append(i)
    return new_list
