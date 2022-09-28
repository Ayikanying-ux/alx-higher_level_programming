#!/usr/bin/python3
def uniq_add(my_list=[]):
    set(my_list)
    number = 0
    for i in my_list:
        number += i
    return number
