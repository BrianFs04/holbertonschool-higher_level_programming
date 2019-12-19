#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sums = 0
    sums2 = 0
    score = [[first*second for first, second in zip(elem, elem[1:])]
             for elem in my_list]
    weight = [[second for second in zip(elem[1:])] for elem in my_list]
    for nums in score:
        for elem in nums:
            sums += elem
    for nums_t in weight:
        for elem1 in nums_t:
            for i in elem1:
                sums2 += i
    return sums / sums2
