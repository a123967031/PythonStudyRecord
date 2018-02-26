#!/usr/bin/env python
#-*- coding : utf-8 -*-
import string

num1 = []
num2 = []
num = raw_input("please input numbers: ")

for i in num:
	num1.append(int(i))
	num2.append(i)

num1.sort()
num1.reverse()
num2.sort()
num2.reverse()

print num1
print num2
