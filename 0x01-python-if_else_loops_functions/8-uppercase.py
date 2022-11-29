#!/usr/bin/python3
def uppercase(str):
    up = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            up += chr(ord(i) - 32)
        else:
            up += " "
    print("{}".format(up))
