#!/usr/bin/env python
#-*- coding:utf-8 -*-

#def max2(num1, num2):
#    if num1 >= num2:
#        return num1
#    else:
#        return num2
#
#def min2(num1, num2):
#    if num1 <= num2:
#        return num1
#    else:
#        return num2

max2 = lambda x,y:x if x>y else y
min2 = lambda x,y:y if x>y else x


def my_max(*my_tuple):
    retval = my_tuple[0]
    for i in my_tuple:
        retval = max2(retval, i)
    return retval

def my_min(*my_tuple):
    retval = my_tuple[0]
    for i in my_tuple:
        retval = min2(retval, i)
    return retval

if __name__ == '__main__':
    print max2(4, 8)
    print min2(4, 8)
    print my_max(2,6,4,8)
    print my_min(2,6,4,8)
    print my_max('av','bd','fd')
    print my_min('av', 'bd', 'fd')
