#!/usr/bin/env python

def printf(tmp, *my_tuple):
    print tmp % my_tuple

printf('%d-%s-%s', 2018, '04', '08')
