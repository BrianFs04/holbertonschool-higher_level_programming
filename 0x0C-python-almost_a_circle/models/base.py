#!/usr/bin/python3
import json


class Base:
    ''' Base class
    '''
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None and len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = '{}.json'.format(cls.__name__)
        if list_objs is None:
            list_objs = []
        with open(filename, "w") as f:
            f.write(cls.to_json_string([cls.to_dictionary(i)
                                        for i in list_objs]))

    def from_json_string(json_string):
        if json_string is None and len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ins = cls(1, 1)
        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        filename = '{}.json'.format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                ready = cls.from_json_string(f.read())
                return [cls.create(**i) for i in ready]
        except:
            return []
