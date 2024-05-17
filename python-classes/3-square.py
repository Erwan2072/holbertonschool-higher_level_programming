#!/usr/bin/python3
""" contain python code """


class Square:
    """ contain Private instance attribute: size"""

    def __init__(self, size=0):
        """ iniitialize size = 0"""
        if not type(size) is int:
            raise Exception("size must be an integer")
        if int(size) < 0:
            raise Exception("size must be >= 0 ")
        self.__size = size

    def area(self):
        """calcul and return surface per square metre"""
        return self.__size ** 2
