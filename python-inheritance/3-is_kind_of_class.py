#!/usr/bin/python3
"""function check if obj is class or an instance of"""


def is_kind_of_class(obj, a_class):
    """check if object is class or an instance of"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
