#!/usr/bin/python3
"""
function that checks state of an object
"""


def is_kind_of_class(obj, a_class):
    """
    function returns true if object is an instance
    of, or if the othe object is an instance of a
    class that inherited from, the specified class ; otherwise False.
    """
    return isinstance(obj, a_class)
