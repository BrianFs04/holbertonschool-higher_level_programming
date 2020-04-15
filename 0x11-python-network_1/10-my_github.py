#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':

    x = requests.get('https://api.github.com/', auth=(sys.argv[1],
                                                       sys.argv[2]))

    print(x.json().get('id'))
