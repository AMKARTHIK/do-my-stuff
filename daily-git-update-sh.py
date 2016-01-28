#!/usr/bin/env python

import commands
import subprocess

REPO_LIST = ['trillium_repolist', 'mm_lafleur_repolist', 'sodexis_repolist']

for repo in REPO_LIST:
    if repo == 'trillium_repolist':
        try:
            update = commands.getoutput(
                "/opt/odoo/8.0/git_update/git_update.sh {0}".format(repo))
            subprocess.Popen(['notify-send', "v8 Repos updated successfully"])
        except exceptions:
            raise subprocess.Popen(
                ['notify-send', "Error in the updation of V8 repos"])
    elif repo == 'mm_lafleur_repolist':
        try:
            update = commands.getoutput(
                "/opt/odoo/9.0/git_update/git_update.sh {0}".format(repo))
            subprocess.Popen(['notify-send', "v9 Repos updated successfully"])
        except exceptions:
            raise subprocess.Popen(
                ['notify-send', "Error in the updation of V9 repos"])
    else:
        subprocess.Popen(
            ['notify-send', "Update Done Please the previous log message to ensure whether the code updated or not"])
