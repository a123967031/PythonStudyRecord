#!/usr/bin/env python
#-*- coding : utf-8 -*-
'''chapter6'''

import string
import random

def min2hour(original):
	hours = int(original) / 60
	minutes = int(original) % 60
	return str(hours)+':'+str(minutes)

def findchr(string,char):
	for i in range(len(string)):
		if string[i] == char:
			return i
	else:
		return -1

def rfindchr(string,char):
	a = -1
	for i in range(len(string)):
                if string[i] == char:
			a = i
        return a

def subchr(string,origchar,newchar):
	stringlst = list(string)
        for i in range(len(string)):
		if stringlst[i] == origchar:
			stringlst[i] = newchar
	return ''.join(stringlst)

def Rochambeau(num):
	'''please choose a number:
	0 : Rock
	1 : Scissor
	2 : Cloth'''
	i = random.randint(0,2)
	a = ['Rock','Scissor','Cloth']
	print 'Computer is '+a[i]
	char = i - num
	if char == 0:
        	return 'draw'
	elif char == -1 or char == 2:
		return 'you fail'
	else:
		return 'you win'


if __name__ == '__main__':
	time = raw_input("input time: ")
	print min2hour(time)
