#!/usr/bin/python3
'''Script that adds all arguments to a Python list
and then save them to a file
'''
import sys
import os

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

listy = []
json_file = 'add_item.json'

if os.path.exists(json_file):
    load_from_json_file(json_file)

for args in sys.argv[1:]:
    listy.append(args)

save_to_json_file(listy, json_file)
