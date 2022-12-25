#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    max_value = 0
    max_name = None
    for key, value in my_dict.items():
        if value > max_value:
            max_value = value
            max_name = key
    return max_name
