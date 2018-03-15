#!/usr/bin/env python
#-*- coding:utf-8 -*-

filename = raw_input('输入文件名')
linenum = input('输入行数')

f = open(filename)
aline = f.readlines()
f.close()
for i in range(linenum):
    print aline[i],
