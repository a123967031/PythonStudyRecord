#!/usr/bin/env python
#-*- coding:utf-8 -*-

def Loopfor(i, end, increment):
    while i <= end:
        print i 
        i += increment

if __name__ == '__main__':
    Loopfor(input("start: "), input("end: "), input("step: "))
