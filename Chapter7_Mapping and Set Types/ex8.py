#!/usr/bin/env python
#-*- coding:utf-8 -*-

mydict1 = {}
mydict2 = {}

while True:
    name = raw_input('输入员工姓名: ')
    if name == '--':
        break
    number = raw_input('输入员工编号: ')
    mydict1[name] = number
    mydict2[number] = name
for key in sorted(mydict1):
    print key,mydict1[key]
print
for key in sorted(mydict2):
    print key,mydict2[key]
