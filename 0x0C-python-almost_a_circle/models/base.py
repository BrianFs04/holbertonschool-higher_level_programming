#!/usr/bin/python3
''' Base class
'''
import json


class Base:
    ''' Base class
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' To json string
        '''
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' Save to json file
        '''
        filename = '{}.json'.format(cls.__name__)
        if list_objs is None:
            list_objs = []
        with open(filename, "w") as f:
            f.write(cls.to_json_string([cls.to_dictionary(i)
                                        for i in list_objs]))

    def from_json_string(json_string):
        ''' From json to string
        '''
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        ''' Returns an instance with all attributes
        '''
        from models.square import Square
        from models.rectangle import Rectangle
        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        if cls is Square:
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        ''' Returns a list of instances
        '''
        filename = '{}.json'.format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                ready = cls.from_json_string(f.read())
                return [cls.create(**i) for i in ready]
        except:
            return []
