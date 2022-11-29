#!/usr/bin/python3
def uppercase(str):
    up = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            up += chr(ord(i) - 32)
        elif ord(i) >= 65 and ord(i) <= 90:
            up += i
        else:
            up += " "
    print("{}".format(up))
