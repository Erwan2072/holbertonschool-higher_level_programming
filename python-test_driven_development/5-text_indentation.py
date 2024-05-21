#!/usr/bin/python3
"""
This function indents a given text. It inserts a newline after each occurrence
    of '.', '?', or ':', and removes any spaces that follow these characters.

    Args:
    text (str): The text to be indented.

    Raises:
    TypeError: If the input text is not a string.

"""


def text_indentation(text):
    """
    indenting a text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    sp_chr = {".", "?", ":"}
    while i < len(text):
        print(text[i], end='')
        if text[i] in sp_chr:
            print("\n")
            while (i + 1 < len(text) and text[i + 1] == ' '):
                i += 1
        i += 1
