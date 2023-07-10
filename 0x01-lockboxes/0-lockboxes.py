#!/usr/bin/python3
"""
This modeule supplies the function `canUnlockAll` which
analyses a list of lockboxes
"""


def canUnlockAll(boxes):
    """
    This function checks and unlocks other locked boxes
    """
    if not boxes or type(boxes) is not list:
        return False

    unlocked = [0]
    for n in unlocked:
        for key in boxes[n]:
            if key not in unlocked and key < len(boxes):
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
