#!/usr/bin/python3
from sys import argv


def main():
    data = len(argv)
    print("{:d} {:s}{:s}".format(data - 1, "argument" if data <= 2 else "arguments",
                                 "." if data == 1 else ":"))
    for i, s in enumerate(argv):
        if i > 0:
            print("{:d}: {:s}".format(i, s))


if __name__ == "__main__":
    main()
