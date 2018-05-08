#!/usr/bin/env python

mins = int(input('> '))
def fmttime(minutes):
    HH = minutes/60
    MM = minutes%60
    print '%d total minutes is %d hour %d min' %(minutes, HH, MM)
fmttime(mins)
