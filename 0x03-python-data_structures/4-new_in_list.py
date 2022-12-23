#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = []
    for i in my_list:
        if i == idx:
            new_list[i] = element
        else:
            new_list[i] = my_list[i]
    return new_list
