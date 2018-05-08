#!/usr/bin/env python

import time

def testit(func, *nkwargs, **kwargs):
    timebefore = time.time()
    retval = func(*nkwargs, **kwargs)
    timeafter = time.time()
    return retval, timeafter-timebefore

def test():
    funcs = (int, long, float)
    vals = (1234, 12.34, '1234')
    for eachFunc in funcs:
        print '-'*80
        for eachVal in vals:
            result = testit(eachFunc, eachVal)
            print '%s(%s) = ' %(eachFunc.__name__, eachVal), result[0], '. time is ', result[1]

if __name__ == '__main__':
    test()
