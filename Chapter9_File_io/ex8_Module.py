#!/usr/bin/env python
#-*- coding:utf-8 -*-

module = raw_input('输入模块名：')
m1 = __import__(module)
m2 = dir(m1)
print m2
for i in m2:
    print 'name: ',i
    print 'type: ', type(getattr(m1, i))
    print 'value: ', getattr(m1, i)
    print
