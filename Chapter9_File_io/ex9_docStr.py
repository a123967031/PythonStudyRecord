#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os

pymodule={}
path = r'/usr/lib/python2.7'
pyfiles = [f for f in os.listdir(path) if endswith('.py')]
for f in pyfiles:
    module=f[:-3]
    pymodules.setdefault(module, '')
    pyfile = path+os.sep+f
    fobj=open(pyfile)
    doc = False
    for line in fobj:
        if line.strip().startswith('__doc__')
