#!/home/harmony/Desktop/Karthik/karthik/DO-MY-STUFF/.venv/bin/python

import argparse
import os
import subprocess
from pprint import pprint as pp
from pygit2 import Repository, GIT_STATUS_CURRENT, discover_repository

parser = argparse.ArgumentParser()
parser.add_argument("base", help="Enter port of the running server.")
args = parser.parse_args()
base_path = os.path.abspath(args.base)

repo_list = []
for root, folders, files in os.walk(base_path, topdown=True):
    if '.git' in folders:
        repo_list.append(root)

unclean_repo = {}
for repo in repo_list:
    real_repo = Repository("{0}/{1}".format(repo,'.git'))
    status = real_repo.status()
    for filepath, flags in status.items():
        if not real_repo.path_is_ignored(filepath):
            if flags != GIT_STATUS_CURRENT:
                if repo in unclean_repo:
                    unclean_repo[repo].append(filepath)
                else:
                    unclean_repo[repo] = [filepath]
for path, files in unclean_repo.iteritems():
    print "Repo {} contains some changed files".format(path)
    for f in files:
        print f
    print "\n"

