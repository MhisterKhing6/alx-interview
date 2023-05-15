#!/usr/bin/python3
"""
Creates a function for the open boxes
"""


def canUnlockAll(containrs):
    """
    Checks if all boxes are open
    """
    if not containrs or type(containrs) is not list:
        return False

    opened_box = [0]
    for n in opened_box:
        for key in containrs[n]:
            if key not in opened_box and key < len(containrs):
                opened_box.append(key)
    if len(opened_box) == len(containrs):
        return True
    return False
