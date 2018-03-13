#!/usr/bin/env python

import getpass
import sys

p = 'Password:'

while True :
   pass1 = getpass.getpass(p)
   pass2 = raw_input('Repeat:')
   if (pass1 == pass2):
      break
   print('Type identical passwords')
print 'All good'

### incomplete
