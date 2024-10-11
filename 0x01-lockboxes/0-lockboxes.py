#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """def doc"""
    n = len(boxes)
    opened = [False] * n  # list to track boxes
    opened[0] = True  # first box is unlocked always
    keys = [0]  # the keys we have started from 0

    while keys:
        key = keys.pop(0)  # take key from the keys list
        for new_key in boxes[key]:  # we get the keys from the opend box
            if new_key < n and not opened[new_key]:  # if the new box not opend
                opened[new_key] = True  # we open it
                keys.append(new_key)  # we add the key to the keys list

    return all(opened)  # return True if all boxes are opened
