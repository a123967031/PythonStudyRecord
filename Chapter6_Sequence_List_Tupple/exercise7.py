#!/usr/bin/env python
#-*- coding : utf-8 -*-

num_str = raw_input()

num_num = int(num_str)

fac_list = range(1,num_num+1)
print "BEFORE:", fac_list

i = 0

while i < len(fac_list):
	if num_num % fac_list[i] == 0:
		del fac_list[i]
	else:
		i = i + 1

print "AFTER:", fac_list
