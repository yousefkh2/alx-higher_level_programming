#!/usr/bin/python3
"""append to a file"""

def append_write(filename="", text=""):
    """append to a file
    
    Args:
    filename: filename
    text: what to append

    Returns
    the number of characters
    """

    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
