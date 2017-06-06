#!/usr/bin/env python

import commands
import os
import pdb
from pprint import pprint


SOURCE_DIR = "/opt/odoo/9.0-SOH/community_modules"
DEST_DIT = "/opt/odoo/9.0-SOH/community_modules_links"


EXCLUDE_PREFIXES = ['.settings', '.git', 'setup', '.project',
                    '.pydevproject', '.bzr']  # list of exclusion prefixes
dir_list = [x for x in next(os.walk(SOURCE_DIR))[1]
            if x not in EXCLUDE_PREFIXES]

check_links_folders = {}

for d in dir_list:
    d_dir = "{0}/{1}".format(SOURCE_DIR, d)
    d_list = [x for x in next(os.walk(d_dir))[1] if x not in EXCLUDE_PREFIXES]
    check_links_folders.update({d: d_list})

# pprint(check_links_folders)

for key, val in check_links_folders.iteritems():
    for v in val:
        link = "{0}/{1}".format(DEST_DIT, v)
        if not os.path.islink(link):
            src = "{0}/{1}/{2}".format(SOURCE_DIR, key, v)
            dst = link
            os.symlink(src, dst)
            print "softlinks created from {0} to {1}".format(src, dst)

# temp_dir_list = [x for x in next(os.walk("{0}/{1}".format(EXCLUDE_PREFIXES, dir_list[0])))[1] if x not in EXCLUDE_PREFIXES]

# print temp_dir_list


# print [name for name in os.listdir(SOURCE_DIR) if os.path.isdir(name)]

# for dirpath, dirnames, filenames in os.walk(SOURCE_DIR):
#     # exclude all dirs starting with exclude_prefixes
#     dirnames[:] = [dirname
#                    for dirname in dirnames
#                    if all([dirname.startswith(string) is False
#                           for string in exclude_prefixes])
#                    is True]
#     print dirnames
# a = os.walk(SOURCE_DIR)
# print type(a)
# dir_list = [x for x in next(os.walk(SOURCE_DIR))[1] if x not in exclude_prefixes]
# print dir_list
# for path, dirs, files in os.walk(SOURCE_DIR):
#     if exclude_prefixes in dirs:
#         dirs.remove(exclude_prefixes)
#
#     print dirs)


# for dirnames in next(a)[1]:
#     print dirnames

# print os.listdir(SOURCE_DIR)

# print os.path.isdir(os.listdir(SOURCE_DIR))
# print next(os.walk(SOURCE_DIR))[1]

# for root, dirs, files in os.walk(SOURCE_DIR):
#     print root


# root_dir = (commands.getoutput(
#     "find {0} -maxdepth 1 -type d -not -path {0} -not -path '{0}/.*'".format(SOURCE_DIR))).split()


# for dir_list in root_dir:
#     print (os.path.basename(dir_list))


#  = root_dir.split()
# print a
#
# # dir_root_dir = []
#
# # print a
# dir_root_dir_name = []
#
# for b in a:
#     list_dir_name = commands.getoutput(
#         "find {0} -maxdepth 1 -type d -not -path {0} -not -path '{0}/.*' -not -path '{0}/.git' -not -path '{0}/.bzr' -printf '%f\n'".format(b))
#     temp_1 = list_dir_name.split()
#     for t1 in temp_1:
#         dir_root_dir_name.append(t1)
#
# for d in dir_root_dir_name:
#     print d
# pdb.set_trace()
# if os.path.islink("{0}/{1}".format(DEST_DIT, dir_root_dir_name[0])):
#     print "True"
# else:
#     print False


# else:
#     print "False"
