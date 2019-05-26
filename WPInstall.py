#!/usr/bin/env python

import subprocess
import os

websiteName = raw_input("What would you like to name your website: ")
os.mkdir(websiteName)
os.chdir(websiteName)
coreCmd = ['wp', 'core', 'download']
subprocess.call(coreCmd)

