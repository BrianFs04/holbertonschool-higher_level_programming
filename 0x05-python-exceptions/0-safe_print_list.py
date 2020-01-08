#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in my_list[:x]:
            print("{}".format(i), end='')
    except:
        pass
    finally:
        print('')
        return i
