#!/usr/bin/env python
#-*- coding: utf-8
p = True
while p:
	a = input("enter a number between 1 to 100:")
	if a >= 1 and a <= 100:
		p = False
	else:
		print("try again!")
