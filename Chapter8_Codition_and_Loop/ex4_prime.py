#!/usr/bin/env python

def isprime(x):
    for i in range(2,x):
        if x%i == 0:
            return True
    else:
        return False

if __name__ == '__main__':
    print isprime(input('> '))
