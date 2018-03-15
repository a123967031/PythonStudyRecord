#!/usr/bin/env python
#-*- coding:utf-8 -*-

filename = raw_input('输入')
f = open(filename, 'r')
alllines = f.readlines()
f.close()
print len(alllines)
