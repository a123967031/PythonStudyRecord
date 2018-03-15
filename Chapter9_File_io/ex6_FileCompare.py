#!/usr/bin/env python
#-*- coding:utf-8 -*-

f1 = open('test.txt', 'r')
f2 = open('test1.txt', 'r')
rows = 0
cols = 0

for line1 in f1:
    rows += 1
    line2 = f2.readline()
    cols = 0
    for i in range(max(len(line1),len(line2))):
        cols += 1
        if cmp(line1[i],line2[i]) != 0:
            print '%drow, %dcol' %(rows, cols)
            break
        else:
            continue
