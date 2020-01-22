#!/usr/bin/python3
import json
from io import StringIO


def save_to_json_file(my_obj, filename):
    '''Writes an Object to a text file
    using a JSON representation
    '''
    with open(filename, 'w') as f:
        return(json.dump(my_obj, f))