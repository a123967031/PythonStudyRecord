#!/usr/bin/env python
#-*- coding : utf-8 -*-

import string
import keyword

alphas = string.letters + '_'
nums = string.digits
keywords = keyword.kwlist
checklst = alphas + nums

print 'Welcome to the Identifier Checker v1.0'
myInput = raw_input('Identifier to test? ')

if myInput in keywords:
	print 'Okay as a keyword'

elif len(myInput) == 1:
	if myInput in alphas:
		print 'Okay as an Identifier'
	else:
		print 'invaild: one symbols must be alphanumeric '
elif len(myInput) > 1:
	if myInput[0] not in alphas:
		print '''invalid: first symbol must be alphabetic'''
	else:
		for otherChar in myInput[1:]:

			if otherChar not in checklst:
				print '''invalid:remaining symbols must be alphanumeric'''
				break
		else:
			print '''okay as an identifier'''

