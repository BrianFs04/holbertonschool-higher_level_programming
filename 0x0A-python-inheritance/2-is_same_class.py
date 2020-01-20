#!/usr/bin/python3
def is_same_class(obj, a_class):
    '''Returns:
    True if the object is exactly an instance
    of the specified class
    False otherwise
    '''
    if isinstance(obj, a_class) and issubclass(a_class, obj.__class__):
        return True
    else:
        return False
