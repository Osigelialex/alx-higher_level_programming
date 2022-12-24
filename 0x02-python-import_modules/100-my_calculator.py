#!/usr/bin/python3

def calculate(count, a, op, b):
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif op not in "*/-+":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if op == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
        if op == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
        if op == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
        if op == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

if __name__ == "__main__":
    from calculator_1 import add, mul, div, sub
    from sys import argv
    calculate(len(argv) - 1, int(argv[1]), argv[2], int(argv[3]))
