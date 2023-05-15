#!/usr/bin/python3
"""
Generating Finobacci numbers
"""
from typing import List


def pascal_triangle(n: int) -> List:
    """
    pascal_triangle- : Get the pascal integers of a number
    n : the number of numbers
    returns : List[List[int]] of the number
    """
    if n <= 0:
        return []
    container = [[1]]
    for j in range(n):
        new = []
        for i in range(len(container[j])):
            if i == 0:  # if it is first elemet just add it
                new.append(container[j][i])
            else:
                new.append(container[j][i] + container[j][i-1])
        new.append(container[j][len(container[j]) - 1])   # add the las element
        container.append(new)
    return container
