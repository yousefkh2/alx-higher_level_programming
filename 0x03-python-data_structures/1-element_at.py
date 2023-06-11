#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrieve element from lidt with index like C

    Args:
        my-list: the list to retrieve from
        idx: the index to retrieve

    Returns:
        None if idx is negative or out of range
        the value in idex if found
    """
    if idx < 0:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
