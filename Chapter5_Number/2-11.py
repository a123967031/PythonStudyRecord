#!/usr/bin/env python
#-*-coding:utf-8
def sum5():
	total = 0
	for i in range(5):
		total += input("enter a number:")
	print "total = %d" %(total)

def average5():
	total = 0
	for i in range(5):
		total += float(input("enter a number:"))
	print "average = %d" %(total/5)
	
while True:
	print '''
Please input 1 to get the total of 5 numbers
Please input 2 to get the average of 5 numbers
Please input x to quit
'''
	choice = raw_input()
	if choice == "1":
		sum5()
	elif choice == "2":
		average5()
	elif choice == "x":
		break
