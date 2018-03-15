#!/usr/bin/env python
#-*- coding: utf-8
while True:
	print "please input a = "
	a = input()
	if a>0:
		print "输入的是正数!"
	elif a<0:
		print "输入的是负数!"
		break
	else:
		print "输入的是零!"
		break
