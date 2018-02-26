#!/usr/bin/env python
#-*- coding:utf-8 -*-

def tr(srcstr, dststr, string, flag):
    mylist = []
    if flag == True:
        dicta = dict(zip(srcstr.lower(), dststr.lower()))
        if len(srcstr) > len(dststr):
            dicta.update({}.fromkeys(srcstr[len(dststr):]))
        for mychr in string:
            if mychr in dicta:
               mylist.append(dicta[mychr])
            else:
               mylist.append(mychr)
    else:
        dicta = dict(zip(srcstr, dststr))
        if len(srcstr) > len(dststr):
            dicta.update({}.fromkeys(srcstr[len(dststr):]))
        for mychr in string:
            if mychr in dicta:
                mylist.append(dicta[mychr])
            else:
                mylist.append(mychr)
    mylist = [ch for ch in mylist if ch] #将字符串中NoneType字符过滤
    print ''.join(mylist)

if __name__ == '__main__':
    src = raw_input("input src: ")
    dst = raw_input("input dst: ")
    string = raw_input("input string: ")
    flag = raw_input("input False or True: ")
    tr(src, dst, string, flag)
