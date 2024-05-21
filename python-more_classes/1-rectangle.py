#!/usr/bin/python3
""" containpython code"""


class Rectangle:
    """contain a simple class of rectangle"""

    def __init__(self, height=0, width=0):
        self.width = width
        self.height = height

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(width, int):
                raise TypeError("width must be an integer")
            if width < 0 :
                raise ValueError("width must be >= 0")
            self.__width = width

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(height, int):
                raise TypeError("height must be an integer")
            if height < 0 :
                raise ValueError("height must be >= 0")
            self.__height = height

