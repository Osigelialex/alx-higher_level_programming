#!/usr/bin/python3

"""
function checks if obj is a subclass
"""


def inherits_from(obj, a_class):
    """
    function() : inherits_from
    returns True if an object inherited from
    a class, otherwise False
    """

    return isinstance(obj, a_class) and issubclass(type(obj), a_class)
