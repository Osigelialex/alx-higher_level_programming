#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = 0
    denominator = 0
    average = 0
    for i in my_list:
        numerator += i[0] * i[1]
        denominator += i[1]
    average = numerator / denominator
    return average
