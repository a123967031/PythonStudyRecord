#!/usr/bin/env python
# -*- coding:utf-8 -*-

f = open('scores.txt', 'r')
scores = []
for eachline in f:
    if 0<= int(eachline.strip())<=100:
        scores.append(int(eachline.strip()))
    if int(eachline.strip())<60:
        print 'score is F', eachline
    elif int(eachline.strip())<70:
        print 'score is D',eachline
    elif int(eachline.strip())<80:
        print 'score is C', eachline
    elif int(eachline.strip())<90:
        print 'score is B', eachline
    elif int(eachline.strip())<=100:
        print 'score is A', eachline
    else:
        print 'score wrong!', eachline
f.close()
print 'average score is %f' %(sum(scores)//len(scores))
