#!/usr/bin/env python

def getfactors(x):
    factor = []
    for i in range(1,x+1):
        if x%i == 0:
            factor.append(i)
    return factor

if __name__ == '__main__':
    print getfactors(input('> '))
