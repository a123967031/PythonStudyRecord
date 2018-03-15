#!/usr/bin/env python
#-*- coding:utf-8 -*-

F = raw_input('输入文件名：')
f = open(F, 'r')
index = 0
for eachline in f:
    index += 1
    if index%26 != 0:
        print eachline,
    else:
        raw_input('...按任意键继续')
