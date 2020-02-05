#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''Prints a list
    '''
    ind = 0
    try:
        for i in range(x):
            print("{}".format(my_list[ind]), end='')
            ind += 1
    except IndexError:
        pass
    finally:
        print('')
        return ind
