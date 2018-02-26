#!/usr/bin/env python
#-*- coding : utf-8 -*-
import string


def stripblank(string):
	for i in range(len(string)):
		if string[i] != " ":
			a = i
			break
	for i in range(1,len(string)+1):
		if string[-i] != ' ':
			b = -i
			break
	if b+1 == 0:
		print string[a:]
	else:
		print string[a:b+1]




if __name__ == '__main__':
	inputstr = raw_input('input a string: ')
	stripblank(inputstr)
