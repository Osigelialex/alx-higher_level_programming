#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff_1 = set(filter(lambda x: x not in set_2, set_1))
    diff_2 = set(filter(lambda x: x not in set_1, set_2))
    return diff_1.union(diff_2)
