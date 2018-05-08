#!/usr/bin/env python

def LeapYear(year):
    if (year%4 == 0 and year%100 != 0) or year%400 ==0:
        print '%d year is leap year!' %year
        return True
    else:
        return False

if __name__ == '__main__':
    yearlist = range(1000,2000)
    print filter(LeapYear, yearlist)
    print [i for i in range(1000,2000) if (i%4 == 0 and i%100 != 0) or i%400 ==0]
