#!/usr/bin/env python

import commands
import os
from pprint import pprint
from sys import argv

script, source, dest, name = argv
OKBLUE = '\033[94m'
ENDC = '\033[0m'
FAIL = '\033[91m'


SOURCE = os.path.abspath(source)
DEST_DIR = os.path.abspath(dest)

link = "{0}/{1}".format(DEST_DIR, name)
if not os.path.islink(link):
    src = SOURCE
    dst = link
    os.symlink(src, dst)
    print "softlinks created from {2}{0}{3} to {2}{1}{3}".format(src,
            dst,OKBLUE,ENDC)
