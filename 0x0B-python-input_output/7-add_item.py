#!/usr/bin/python3
'''
Adds all program arguments to a list and save it
to JSON file
'''


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

my_l = []
try:
    my_l = load_from_json_file("add_item.json") + argv[1:]
    save_to_json_file(l, "add_item.json")
except Exception:
    save_to_json_file(l, "add_item.json")
