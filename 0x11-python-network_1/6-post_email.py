#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter"""
import requests
import sys


if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    x = requests.post(sys.argv[1], data)
    print(x.text)
