#!/usr/bin/env python

def sum100(x):
    if x>0:
        return sum100(x-1)+x
    else:
        return 0

def Fibonacci1(x):
    if x>2:
        return Fibonacci1(x-1) + Fibonacci1(x-2)
    else:
        return 1

def Fibonacci2(x,a,b):
    if x>2:
        return Fibonacci2(x-1, b, a+b)
    else:
        return b

if __name__ == '__main__':
#    print sum100(100)
    print Fibonacci1(8)
    print Fibonacci2(8,1,1)
