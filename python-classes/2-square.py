#!/usr/bin/python3
""" contain python code """


class Square:
    """ contain Private instance attribute: size"""

    def __init__(self, size=0):
        if not type(size) is int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
