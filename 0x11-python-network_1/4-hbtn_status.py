#!/usr/bin/python3
"""Script that fetches a URL"""
import requests

if __name__ == "__main__":
    x = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(str(x))))
    print("\t- content: {}".format(x.text))
    x.close()
