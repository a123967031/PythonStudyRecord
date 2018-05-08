#!/usr/bin/env python

def average(a, b):
    return (a+b)/2


myset = {1, 2, 4, 5}
print reduce(average, myset)
