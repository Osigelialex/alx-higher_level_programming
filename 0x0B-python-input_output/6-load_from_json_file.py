#!/usr/bin/python3
"""
function that creates object from a JSON file
"""

import json


def load_from_json_file(filename):
    """
    module load_from_json_file
    """

    with open(filename) as f:
        return json.loads(f)
