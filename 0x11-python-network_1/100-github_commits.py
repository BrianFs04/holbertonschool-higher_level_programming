#!/usr/bin/python3
"""Gets the last 10 commits of a GitHub repo"""
import requests
import sys

if __name__ == '__main__':

    x = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(sys.argv[2], sys.argv[1]))
    jso = x.json()

    for i in jso[:10]:
        sha = i.get('sha')
        author = i.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
