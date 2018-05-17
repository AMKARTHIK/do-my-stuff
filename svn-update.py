#!/usr/bin/env python

import argparse
import subprocess
import getpass
from dotenv import load_dotenv
load_dotenv()
try:
    import pysvn
except ImportError:
    subprocess.call('sudo apt-get install python-svn', shell=True)
    import pysvn
import os


parser = argparse.ArgumentParser()
parser.add_argument("source", help="Path that contains svn repos")
args = parser.parse_args()
SOURCE_DIR = args.source



path_list = []
for root, dirs, files in os.walk(SOURCE_DIR):
    for name in dirs:
        if name.endswith((".svn")):
             abs_path = path_list.append(os.path.join(root, name).replace('/.svn',''))


# check status of current dir

not_updated = []
#updated = []
def get_login(realm=True, username='karthik', may_save=True):
    password = os.environ.get('SVN_PASS') or getpass.getpass()
    return True, 'karthik', password, True
client = pysvn.Client()
client.callback_get_login = get_login

for path in path_list:
    print "=================================================="
    print "Updating the path ", path
    print "==================================================\n"

    changes = client.status(path)

    added_files = [f.path for f in changes if f.text_status == pysvn.wc_status_kind.added]
    deleted_files = [f.path for f in changes if f.text_status == pysvn.wc_status_kind.deleted]
    modified_files = [f.path for f in changes if f.text_status == pysvn.wc_status_kind.modified]
    conflicted_files = [f.path for f in changes if f.text_status == pysvn.wc_status_kind.conflicted]

    if any([added_files, deleted_files, modified_files, conflicted_files]):
        not_updated.append(path)
        print "This path contains some conflicts. Solve it and updated it manually or by script", path
        print "\n========================================================================\n"
    elif not any([added_files, deleted_files, modified_files, conflicted_files]):
        remote_rev = client.revpropget("revision", url=client.root_url_from_path(path))[0].number
        local_rev = client.info(path).get("revision").number
        if remote_rev > local_rev:
            client.update(path)
            print "This repo updated sucessfully from {0} revision to {1} revision".format(local_rev, remote_rev)
            print "\n========================================================================\n"
        else:
            print "This repo was already upto date ..."
            print "\n======================================================================\n"


if not_updated:
    print "========================================================="
    print not_updated
#print "Not Updated"
#print not_updated

#print "===================================================================="
#print "updated"
#print updated
