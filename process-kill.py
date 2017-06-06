#!/usr/bin/env python

import commands

pid_kill = commands.getoutput("pgrep odoo")
print pid_kill

kill_it = commands.getoutput("sudo kill -9 {0}".format(pid_kill))
