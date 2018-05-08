#!/usr/bin/env python
#-*- coding:utf-8 -*-
'''清洗文件，输入文件名，除去每行所有排头和最尾的空白'''

import os

def clean(filename):
    print '(c)reate a new file'
    print '(o)verwrite the original file'
    op = raw_input()
    if op.lower() == 'c':
        newfilename = raw_input('input a new file name: ')
        oldfile = open(filename, 'r')
        newfile = open(newfilename, 'w')
        lines = map((lambda line:line.strip()), oldfile)
        #lines = [line.strip() for line in oldfile]
        for line in lines:
            newfile.write(line)
            newfile.write(os.linesep)
        oldfile.close()
        newfile.close()
    elif op.lower() == 'o':
        oldfile = open(filename, 'r')
        lines = map((lambda line:line.strip()), oldfile)
        #lines = [line.strip() for line in oldfile]
        oldfile.close()
        oldfile = open(filename, 'w')
        for line in lines:
            oldfile.write(line)
            oldfile.write(os.linesep)
        oldfile.close()
    else:
        print 'error!'

clean('test.txt')
