#!/usr/bin/python3

def add():
    length = len(argv)
    sum = 0

    for i in range(1, length):
        sum += int(argv[i])
    
    print("{:d}".format(sum))

if __name__ == "__main__":
    from sys import argv
    add()
