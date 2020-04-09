#!/usr/bin/python3
""" Function to find a peak """


def find_peak(list_of_integers):
    """Find peak method"""
    if list_of_integers:
        length = len(list_of_integers)
        peak = list_of_integers[0]
        if list_of_integers[0] > list_of_integers[1]:
            peak = list_of_integers[0]
        elif list_of_integers[length - 1] > list_of_integers[length - 2]:
            peak = list_of_integers[length - 1]
        else:
            for i in range(length - 1):
                if list_of_integers[i] > list_of_integers[i+1] and\
                   list_of_integers[i] > list_of_integers[i-1]:
                    peak = list_of_integers[i]
        return peak
