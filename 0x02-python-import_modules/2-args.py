#!/usr/bin/python3

def print_arguments():
    length = len(argv) - 1
    
    if length == 0:
        print("{:d} arguments.".format(length))
    if length == 1:
        print("{:d} argument:".format(length))
        print("{:d}: {:s}".format(length, argv[length]))
    if length > 1:
        print("{:d} arguments:".format(length))
        for i in range(1, length):
            print("{:d}: {:s}".format(i, argv[i]))

if __name__ == "__main__":
    from sys import argv
    print_arguments()
