#!/usr/bin/python3
"""A module that defines a class MyList"""

class MyList(list):
    """
        MyList inherits from list
        that prints the list, but sorted
    """


    def print_sorted(self):
        """print list"""


        sorted_list = sorted(self)

        for i in self:
            if type(i) is not int:
                raise TypeError("failed mission")
        print(sorted_list)
