#!/usr/bin/env python3
"""Pickling Custom Classes"""

import pickle


class CustomObject:
    """Serializes the current instance of
        CustomObject to the specified file.
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Deserializes an instance of CustomObject from the specified file.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Serialization error: {e}")

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                if isinstance(obj, cls):
                    return obj
                else:
                    print("Deserialized object is not of type CustomObject.")
                    return None
        except Exception as e:
            print(f"An error occurred while deserializing the object: {e}")
            return None
