#!/usr/bin/env python
#-*- coding:utf-8 -*-

def factorial(N):
    temp = 1
    for i in range(1,N+1):
        temp *= i
    return temp

if __name__ == '__main__':
    print factorial(input('> '))
