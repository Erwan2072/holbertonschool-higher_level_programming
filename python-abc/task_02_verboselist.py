#!/usr/bin/env python3
"""create a class named Verboselist ext python"""

class VerboseList(list):
    def append(self, element):
        super().append(element)
        print("Added [{}] to the list".format(element))

    def extend(self, extended):
        nb_element = len(extended)
        super().extend(extended)
        print("Extended the list with [{}] items".format(nb_element))

    def remove(self, element):
        print("Removed [{}] from the list.".format(element))
        super().remove(element)

    def pop(self, index=-1):
        element = super().pop(index)
        print("Popped [{}] from the list.".format(element))
        return element
