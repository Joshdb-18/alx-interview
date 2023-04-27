#!/usr/bin/python3
"""
LockBoxes
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be openes
    """
    num_boxes = len(boxes)
    keys = [0] + boxes[0]
    opened = [False] * num_boxes
    opened[0] = True

    while True:
        new_boxes = False
        for i in range(num_boxes):
            if not opened[i] and i in keys:
                keys += boxes[i]
                opened[i] = True
                new_boxes = True
        if not new_boxes:
            break

    return all(opened)
