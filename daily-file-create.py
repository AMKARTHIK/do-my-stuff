#!/usr/bin/env python

import os
import commands
from datetime import datetime

TODAYDATE = datetime.now()
FILENAME = TODAYDATE.strftime("%m%d%Y")

FILE_EXIST = os.path.exists("/home/harmony/Desktop/Karthik/karthik/Text-File/Da\
ily-Works/{0}".format(FILENAME))


if not FILE_EXIST:
    commands.getoutput("touch /home/harmony/Desktop/Karthik/karthik/Text-File/Da\
ily-Works/{0}".format(FILENAME))

    with open("/home/harmony/Desktop/Karthik/karthik/Text-File/Daily-Wo\
rks/Template") as fopen:
        with open("/home/harmony/Desktop/Karthik/karthik/Text-File/Daily-Wor\
ks/{0}".format(FILENAME), "w") as fwrite:
            fwrite.writelines(fopen.readlines())
