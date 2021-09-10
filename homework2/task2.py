"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.
You may assume that the array is non-empty and the most common element
always exist in the array.
Example 1:
Input: [3,2,3]
Output: 3, 2
Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2, 1
"""

from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    total = {}
    for el in inp:
        total[el] = inp.count(el)
    lst_el = list(total.items())
    lst_el.sort(key=lambda i: i[1], reverse=True)
    return lst_el[0][0], lst_el[-1][0]
