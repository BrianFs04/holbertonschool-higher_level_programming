#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""
import requests
import sys


if __name__ == "__main__":
    x = requests.get(sys.argv[1])
    err_code = int(x.status_code)
    if (err_code >= 400):
        print("Error code: {}".format(x.status_code))
    else:
        print(x.text)
