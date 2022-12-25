#!/usr/bin/python3

def best_score(a_dictionary):
    #if dictionary is empty
    if a_dictionary is None:
        return None
    max = 0
    name = ""
    for i in a_dictionary:
        if a_dictionary[i] > max:
            name = i
    return name
