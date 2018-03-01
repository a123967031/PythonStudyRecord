#!/usr/bin/env python
#-*- coding:utf-8 -*-


import datetime

def isperfect(x):
    if sum(i for i in range(1, x) if (x%i == 0)) == x:
        return True
    else: return False

if __name__ == '__main__':
    start = datetime.datetime.now()
    a = input('> ')
    for j in range(1, a):
        if isperfect(j):
            print j,
    end = datetime.datetime.now()
    timex = end - start
    print
    print "小于%d的所有完全数" %a
    print "花费%s时间" %timex
