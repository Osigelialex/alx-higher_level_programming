#!/usr/bin/python3
def fizzbuzz():
    str = ""
    for i in range(101):
        if i % 3 == 0:
            str += "fizz"
        if i % 5 == 0:
            str += "buzz"
        if str == "":
            print(i, end=" ")
        print("{}".format(str), end=" ")
