#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    rns = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    list_nums = []
    first = 0
    second = 0
    sums = 0
    for chars in roman_string:
        list_nums.append(rns[chars])
    if len(roman_string) == 1:
        return list_nums[0]
    for first, second in zip(list_nums, list_nums[1:]):
        if first < second:
            sums -= first
        else:
            sums += first
    return sums + second
