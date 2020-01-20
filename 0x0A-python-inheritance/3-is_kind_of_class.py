#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    '''Returns:
    True if the object is an instance of a class or
    if it is an instance of a class that is inherited
    False otherwise
    '''
    if isinstance(obj, a_class) and issubclass(obj.__class__, a_class):
        return True
    else:
        return False
