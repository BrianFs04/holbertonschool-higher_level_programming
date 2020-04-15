#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':

    if len(sys.argv) is 1:
        q = ""
    else:
        q = sys.argv[1]

    x = requests.post('http://0.0.0.0:5000/search_user', data = {'q': q})

    try:
        response = x.json()
        if len(response) == 2:
            print("[{}] {}".format(response.get('id'), response.get('name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
