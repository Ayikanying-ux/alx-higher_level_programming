#!/usr/bin/python3
def uniq_add(my_list=[]):
    number = 0
    for i in set(my_list):
        number += i
    return number
