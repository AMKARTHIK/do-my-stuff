#!/home/harmony/Desktop/Karthik/karthik/DO-MY-STUFF/.venv/bin/python

import argparse
import os
import subprocess
from pprint import pprint as pp
from pygit2 import Repository, GIT_STATUS_CURRENT, discover_repository
from colorama import init
from termcolor import colored

init()

parser = argparse.ArgumentParser()
parser.add_argument("base", help="Base path")
parser.add_argument("command", type=str, help="Git command")
args = parser.parse_args()
base_path = os.path.abspath(args.base)

repo_list = []
for root, folders, files in os.walk(base_path, topdown=True):
    if '.git' in folders:
        repo_list.append(root)

for repo in repo_list:
    command = "cd {0} && {1}".format(repo, args.command)
    output = subprocess.check_output(command, shell=True)
    if output:
        print "=" * 30
        print colored("\nExecuting on repo: {}\n".format(repo), 'red')
        print output
