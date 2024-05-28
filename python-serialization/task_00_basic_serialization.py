#!/usr/bin/env python3
"""Basic Serialization"""

import json


def serialize_and_save_to_file(data, filename):
    """
    to serialize and save data to the specified file
    """
    with open(filename, 'w') as file:
        file.write(json.dumps(data))


def load_and_deserialize(filename):
    """deserialize data from the specified file"""
    with open(filename, 'r') as file:
        return json.load(file)
