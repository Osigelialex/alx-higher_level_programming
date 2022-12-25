#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if key is None:
        return a_dictionary
    del(key)
    return a_dictionary
