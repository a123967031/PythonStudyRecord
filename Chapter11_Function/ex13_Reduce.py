#!/usr/bin/env python

def mult(x, y):
    return x*y

#print mult(2,3)

print reduce(mult, range(1,5))

#print reduce(lambda x,y:x*y, range(1,5))
