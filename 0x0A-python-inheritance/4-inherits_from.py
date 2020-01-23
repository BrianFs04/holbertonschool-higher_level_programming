#!/usr/bin/python3
def inherits_from(obj, a_class):
    '''Returns:
    True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class
    False otherwise
    '''
    if type(obj) is not a_class and issubclass(obj.__class__, a_class):
        return True
    else:
        return False
