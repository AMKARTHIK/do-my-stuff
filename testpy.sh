#!/usr/bin/env python

import subprocess
import datetime

now = datetime.datetime.now()

a = now.strftime("%d%m%Y")
#print a
subprocess.call("rm -rf {0}".format(a), shell=True)
