#!/usr/bin/env python

import commands
import os
from pprint import pprint
from sys import argv

script, source, dest = argv


SOURCE_DIR = source
DEST_DIT = dest

if not os.path.isdir(DEST_DIT):
    os.makedirs(DEST_DIT)


EXCLUDE_PREFIXES = ['.settings', '.git', 'setup', '.project',
                    '.pydevproject', '.bzr']  # list of exclusion prefixes
dir_list = [x for x in next(os.walk(SOURCE_DIR))[1]
            if x not in EXCLUDE_PREFIXES]

check_links_folders = {}

for d in dir_list:
    d_dir = "{0}/{1}".format(SOURCE_DIR, d)
    d_list = [x for x in next(os.walk(d_dir))[1] if x not in EXCLUDE_PREFIXES]
    check_links_folders.update({d: d_list})

#pprint(check_links_folders)

for key, val in check_links_folders.iteritems():
    for v in val:
        link = "{0}/{1}".format(DEST_DIT, v)
        if not os.path.islink(link):
            src = "{0}/{1}/{2}".format(SOURCE_DIR, key, v)
            dst = link
            os.symlink(src, dst)
            print "softlinks created from {0} to {1}".format(src, dst)

# delete the broken link

link_list = [x for x in next(os.walk(DEST_DIT))[1]]

#print sorted(link_list)

broken_links = [x for x in next(os.walk(DEST_DIT))[2]]

for blink in broken_links:
    broken_link_path = '{0}/{1}'.format(DEST_DIT, blink)
    os.unlink(broken_link_path)
    print "The {0} link removed from the DEST DIR".format(broken_link_path)
