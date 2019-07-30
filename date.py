#!/home/harmony/Desktop/Karthik/karthik/DO-MY-STUFF/.venv/bin/python

from sys import argv
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pyperclip

script, dd = argv
fo = '%Y-%m-%d'

print datetime.strftime(datetime.strptime(dd, fo) + relativedelta(months=1), fo)
pyperclip.copy(datetime.strftime(datetime.strptime(dd, fo) + relativedelta(months=1), fo))

