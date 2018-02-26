#!/usr/bin/env python
#-*- coding:utf-8 -*-

from string import letters

newlist = []

def encrypt(mystr):
    for mychr in mystr:
        if (mychr in letters[:13]) or (mychr in letters[26:39]):
            mychr = chr(ord(mychr)+13)
        elif (mychr in letters[13:26]) or (mychr in letters[39:]):
            mychr = chr(ord(mychr)-13)
        else:
            pass
        newlist.append(mychr)
    print ''.join(newlist)


if __name__ == '__main__':
    string = raw_input("输入字符串: ")
    encrypt(string)
