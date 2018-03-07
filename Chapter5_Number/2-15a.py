#!/usr/bin/env python
#-*-coding:utf-8
print "Please input 3 numbers"
a = int(raw_input("Please input number a:"))
b = int(raw_input("Please input number b:"))
c = int(raw_input("Please input number c:"))
if a > b:
	a,b = b,a
if a > c:
	a,c = c,a
if b > c:
	b,c = c,b
print a,b,c
