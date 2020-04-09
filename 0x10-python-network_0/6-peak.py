#!/usr/bin/python3
""" Function to find a peak """


def findPeakUtil(arr, low, high):
    """ Find peak"""
    if not arr:
        return None

    mid = int((high + low)/2)

    if ((mid == 0 or arr[mid - 1] <= arr[mid]) and (
            mid == len(arr) - 1 or arr[mid + 1] <= arr[mid])):
        return arr[mid]

    elif (mid > 0 and arr[mid - 1] > arr[mid]):
        return findPeakUtil(arr, low, (mid - 1))

    else:
        return findPeakUtil(arr, (mid + 1), high)


def find_peak(list_of_integers):
    """Find peak method"""
    if not list_of_integers:
        return None

    Max = len(list_of_integers) - 1
    Min = 0
    return findPeakUtil(list_of_integers, Min, Max)
