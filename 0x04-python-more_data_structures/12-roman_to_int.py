#!/usr/bin/python3

def roman_to_int(roman_string):
    syms = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0

    if roman_string is None or type(roman_string) != str or roman_string == "":
        return 0
    for i in range(len(roman_string) - 1):
        if syms[roman_string[i]] < syms[roman_string[i + 1]]:
            num = num + syms[roman_string[i + 1]] - syms[roman_string[i]]
        else:
            num = num + syms[roman_string[i]]
    length = len(roman_string)
    if syms[roman_string[length - 2]] >= syms[roman_string[length - 1]]:
        num = num + syms[roman_string[length - 1]]
    return num
