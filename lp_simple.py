#!/usr/local/bin/python3



import os
import pyotp
from datetime import datetime, timedelta

secret = 'jpqhqyymaie3zk3q'

if __name__ == '__main__':
    if secret:
        totp = pyotp.TOTP(secret)
        now = datetime.now()
        print('OTP at: {0}\n{1}'.format(now, int(totp.at(now))))
