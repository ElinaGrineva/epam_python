"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any, Iterable

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
     },
    "fourth": "RED",
}


def find_occurrences(tree: Iterable, element: Any) -> int:
    counter = 0
    if isinstance(tree, (set, tuple, list)):
        for subtree in tree:
            counter += find_occurrences(subtree, element)
    elif isinstance(tree, dict):
        for key, value in tree.items():
            if key == element:
                counter += 1
            counter += find_occurrences(value, element)
    elif tree == element:
        counter += 1
    return counter