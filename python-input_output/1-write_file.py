#!/usr/bin/python3
""" writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """write function"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return len(text)
