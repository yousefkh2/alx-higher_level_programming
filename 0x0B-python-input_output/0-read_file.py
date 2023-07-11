#!/usr/bin/python3
"""read elements in a file"""

def read_file(filename=""):
    """read elements of a file

    Args:
    filename: filename
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
