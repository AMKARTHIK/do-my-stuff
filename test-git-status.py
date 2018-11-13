#!/usr/bin/env python

import argparse
import os
import subprocess
from pprint import pprint as pp
from pygit2 import Repository, GIT_STATUS_CURRENT

parser = argparse.ArgumentParser()
parser.add_argument("base", help="Enter port of the running server.")
args = parser.parse_args()
base_path = os.path.abspath(args.base)

repo_list = []
for root, folders, files in os.walk(base_path, topdown=True):
    if '.git' in folders:
        repo_list.append(root)

for repo in repo_list:
    print "Repo: {}".format(repo)
    real_repo = Repository("{0}/{1}".format(repo,'.git'))
    status = real_repo.status()
    for filepath, flags in status.items():
        if flags != GIT_STATUS_CURRENT:
            if '.pyc' not in filepath and '__pycache__' not in filepath:
                print "Filepath {} isn't clean".format(filepath)
    print "\n"


