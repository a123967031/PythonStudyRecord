#!/usr/bin/env python
#-*- coding : utf-8 -*-
import string

str1 = raw_input()
str2 = raw_input()

for i,j in zip(str1,str2):
	if i is not j:
		print "no!"
		break
else:
	print "yes!"
