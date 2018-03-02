#!/usr/bin/env python
#-*- coding:utf-8 -*-

def count(mystring):
    yystring = 'aeiou'
    yy = 0
    fy = 0
    for i in mystring:
        if i in yystring:
            yy += 1
        elif i != ' ':
            fy += 1
    key = len(mystring.split())
    print '元音数量: %d\n辅音数量: %d\n单词数: %d' %(yy, fy, key)

if __name__ == '__main__':
    count(raw_input('> '))
