#!/usr/bin/python3
"""Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists
"""

def canUnlockAll(boxes):
    """Determines if all boxes can be unlocked"""
    n = len(boxes)
    keys = {0}
    opened_boxes = [0]

    while opened_boxes:
        current_box = opened_boxes.pop()
        for key in boxes[current_box]:
            if key not in keys and key < n:
                keys.add(key)
                opened_boxes.append(key)

    return len(keys) == n
