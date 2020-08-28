#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics"""
import signal
import sys


def signal_handler(sig, frame):
    """Handles Ctrl+C"""
    print("File size {}".format(size))
    for k, v in sorted(ordered.items()):
        print(k, v)
    sys.exit(0)

if __name__ == "__main__":
    ordered = {}
    size = i = 0
    count = 1
    data = sys.stdin
    for line in data:
        i += 1
        item = line.split(" ")
        st_code = int(item[-2])
        size += int(item[-1])
        if ordered.get(st_code):
            ordered[st_code] += count
        else:
            ordered[st_code] = count
        if i % 10 == 0:
            print("File size {}".format(size))
            for k, v in sorted(ordered.items()):
                print(k, v)
        signal.signal(signal.SIGINT, signal_handler)
