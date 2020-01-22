#!/usr/bin/python3
def pascal_triangle(n):
    listy = []
    listy_con = []

    for i in range(0, n):
        pox = listy
        if i is not 0:
            listy = [1]
        for j in range(1, i):
            listy.append(pox[j - 1] + pox[j])
        listy.append(1)
        listy_con.append(listy)
    return listy_con
