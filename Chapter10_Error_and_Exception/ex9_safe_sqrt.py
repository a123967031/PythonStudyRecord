#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import math
import cmath

def safe_sqrt(value):
    try:
        result = math.sqrt(value)
    except ValueError:
        result = cmath.sqrt(value)
    return result

if __name__ == '__main__':
    print safe_sqrt(1)
    print safe_sqrt(-1)
