#!/usr/bin/env python
#-*- coding:utf-8 -*-

def TrueOpen(filename):
    try:
        f = open(filename, 'r')
    except IOError:
        return None
    return f

if __name__ == '__main__':
    name = raw_input('> ')
    print TrueOpen(name)
