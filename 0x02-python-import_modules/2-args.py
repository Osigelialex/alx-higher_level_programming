#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    length = len(argv)
    if length == 1:
        print("{:d} argument:".format(length))
    elif length < 1:
        print("{:d} arguments.".format(length))
    else:
        for i in range(1, length):
            print("{:d}: {:s}".format(i, argv[i]))
