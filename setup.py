#!/usr/bin python

import os
import subprocess

# check the current user is root or not if not then exit from the execution of
# the script
#if os.getuid() != 0:
#    print "Sorry {0}, you must have Admin privilages to run this script".format(os.getenv('USER'))
#    exit()


# logic starts here

#print "Welcome Sudo User....!!!!"

#PACKAGES_MUST_HAVE = {'pip':'python-pip'}

#for k,v in PACKAGES_MUST_HAVE.iteritems():
#    try:
#        subprocess.call('import {0}'.format(k), shell=True)
#    except ImportError:
#        subprocess.call('apt-get install {0}'.format(v), shell=True)
subprocess.call('apt-get install python-pip')
