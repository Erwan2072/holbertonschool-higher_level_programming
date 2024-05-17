#!/usr/bin/python3
""" contain python code """


class Square:
    """ contain Private instance attribute: size"""

    def __init__(self, size=0):
        """ initialize the square with  the size """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not type(value) is int:
            raise Exception("size must be an integer")
        if value < 0:
            raise Exception("size must be >= 0")
        self.__size = value

    def area(self):
        """calcul and return surface per square metre"""
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        for _ in range(self.size):
            print("#" * self.size)
