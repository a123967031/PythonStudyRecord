#!/usr/bin/env python

mydict1 = {'a': 1, 'b':2, 'c': 3}
mydict2 = {}

for key in mydict1:
#    mydict2[mydict1[key]] = key
    mydict2.setdefault(mydict1[key],key)


print mydict1,mydict2
