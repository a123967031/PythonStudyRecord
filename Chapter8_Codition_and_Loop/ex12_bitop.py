#!/usr/bin/env python
#-*- coding:utf-8 -*-

def bitop(start, end):
    title = 'DEC\tBIN\t        OCT\tHEX\tASCII\n--------------------------'
    if start >= 126 or end <= 33:
        title = 'DEC\tBIN\t        OCT\tHEX\n--------------------'
    print title
    for i in range(start, end+1):
        if i in range(33, 126):
            print i, '\t', bin(i), '\t', oct(i), '\t', hex(i), '\t', chr(i)
        else:
            print i, '\t', bin(i), ' \t', oct(i), '\t', hex(i), '\t'
        '''
        if i >=32 and i <= 126:
            print '%d\t%07d\t\t%o\t%x\t\t%s' %(i,int(bin(i)[2:]),i,i,chr(i))
        else:
            print '%d\t%07d\t%o\t%x' %(i,int(bin(i)[2:]),i,i)
        '''

if __name__ == '__main__':
    print '-----------------'
    bitop(input('     输入起始值: '), input('     输入结束值: '))
