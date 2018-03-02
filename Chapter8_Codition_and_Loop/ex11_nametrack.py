#!/usr/bin/env python
#-*- coding:utf-8 -*-

def nametrack(n):
    namelst = []
    error = 0
    for i in range(1,n+1):
        name = raw_input('请输入第%s个姓名:' %i)
        if len(name.split(',')) == 2:
            namelst.append(name)
        else:
            error += 1
            if error != 3:
                print '错误的格式，请输入:Lastname,Firstname'
                print '您已经输错了%s次' %error
                namelst.append(name)
            else:
                print '你特么会不会用啊!?'
                break
    print '按照姓排序如下：'
    for x in sorted(namelst):
        print x





if __name__ == '__main__':
    n = input('输入姓名数量:')
    nametrack(n)
