#!/usr/bin/env python

f = open('test.txt', 'r')
for eachline in f:
    if eachline[0] == '#':
        continue
    elif '#' in eachline:
        print eachline[:eachline.find('#')]
    else:
        print eachline,
f.close()
