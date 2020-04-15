#!/usr/bin/python3
"""Sends a request to the URL and displays the value of the
   X-Request-Id variable found in the header
"""
import requests
import sys

if __name__ == "__main__":
    x = requests.get(sys.argv[1])
    print(x.headers.get('X-Request-Id'))
