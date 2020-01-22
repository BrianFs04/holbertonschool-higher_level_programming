#!/usr/bin/python3
'''Script that adds all arguments to a Python list
and then save them to a file
'''
import sys
import os

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

listy = []

for args in sys.argv[1:]:
    listy.append(args)

if os.path.exists('add_item.json'):
    load_from_json_file('add_item.json')

save_to_json_file(listy, 'add_item.json')
