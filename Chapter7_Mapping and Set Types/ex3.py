#!/usr/bin/env python

mydict = {'x': 1, 'z': 3, 'y': 2}
for eachkey in sorted(mydict):
	print "key: ", eachkey

for eachkey in sorted(mydict):
	print "key: ", eachkey, " and value: ", mydict[eachkey]

for i, j in sorted(mydict.items(), key=lambda value:value[1]):
	print "%s:%d" %(i,j)
