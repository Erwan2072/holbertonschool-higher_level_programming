#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for char in str:
        if ('a') <= ord(char) <= ('z'):
            new_str += chr(ord(char) - 32)
        else:
            new_str += char
            new_str += '\n'
    print("{}".format(new_str), end="")
