#!/usr/bin/env python

import os
for tmpdir in ('/tmp', r'c: \temp'):
    if os.path.isdir(tmpdir):
        break

else:
    print 'no temp directory available'
    tmpdir = ''

if tmpdir:
    os.chdir(tmpdir)
    cwd = os.getcwd()
    print '*** current temporary directory'
    print cwd

    print '*** creating temporary directory...'
    os.mkdir('example')
    os.chdir
