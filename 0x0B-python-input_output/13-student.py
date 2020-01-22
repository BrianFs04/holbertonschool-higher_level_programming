#!/usr/bin/python3


class Student:
    '''Student class
    '''
    def __init__(self, first_name, last_name, age):
        '''Constructor
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None and type(attrs) is list:
            items = {k: v for k, v in self.__dict__.items() if k in attrs}
            return items
        else:
            return self.__dict__

    def reload_from_json(self, json):
        return self.__dict__.update(json)
