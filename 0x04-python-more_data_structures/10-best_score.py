#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    max_value = 0
    name = ""
    for key, value in my_dict.items():
        if value > max_value:
            max_value = value
            name = key
    return name
