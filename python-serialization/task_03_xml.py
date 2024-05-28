#!/usr/bin/env python3
"""Serializing and Deserializing with XML"""

import xml.etree.ElementTree as ET
import task_03_xml as xml_serialize


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary to an XML file."""

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)

    """Create an ElementTree object from the root element"""
    tree = ET.ElementTree(root)

    """Write the XML tree to the specified file"""
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserializes an XML file to a Python dictionary"""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}

    """Iterate through the XML elements and reconstruct the dictionary"""
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
