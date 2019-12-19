#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    for key in a_dictionary:
        if key not in a_dictionary:
            return None
        else:
            return sorted(a_dictionary.keys())[-1]
