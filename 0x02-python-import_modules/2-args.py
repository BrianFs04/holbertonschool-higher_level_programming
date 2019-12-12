#!/usr/bin/python3
import sys
argv = sys.argv[1:]
if len(argv) == 0:
    print('{} arguments.'.format(len(argv)))
elif len(argv) == 1:
    print('{} argument:'.format(len(argv)))
    print('{}: {}'.format(len(argv), sys.argv[1]), end='\n')
else:
    print('{} arguments:'.format(len(argv)))
    for i in range(len(argv)):
        print('{}: {}'.format(i+1, argv[i]), end='\n')
