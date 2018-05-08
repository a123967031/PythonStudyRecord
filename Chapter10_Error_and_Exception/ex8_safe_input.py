#!/usr/bin/env python
#-*- coding:utf-8 -*-

def safe_input():
    try:
        word = raw_input('> ')
    except (EOFError, KeyboardInterrupt):
        return None
    return word

if __name__ == '__main__':
    print safe_input()
