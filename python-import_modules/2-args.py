#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    nb_arg = len(argv) - 1

    if nb_arg == 0:
        print("0 arguments.")
    if nb_arg == 1:
        print("1 argument:")
    if nb_arg > 1:
        print("{} arguments:".format(nb_arg))

    for i in range(1, nb_arg + 1):
        print("{}: {}".format(i, argv[i]))
