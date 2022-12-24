#!/usr/bin/python3
from calculator_1 import add, mul, div, sub
from sys import argv

if __name__ == "__main__":
    if len(argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[2] not in "*/-+":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = argv[1]
        b = argv[3]

        if argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        if argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        if argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        if argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
