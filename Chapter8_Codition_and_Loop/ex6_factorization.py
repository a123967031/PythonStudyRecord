#!/usr/bin/env python

def isprime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    else:return True

def factorization(x):
    factor = []
    while not isprime(x):
        for i in range(2,x+1):
            if x%i == 0:
                x /= i
                factor.append(i)
                break
    else:
        factor.append(x)
    return factor

if __name__ == '__main__':
    print factorization(input('> '))
