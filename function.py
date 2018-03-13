#!/usr/bin/env python




def f1(a,b):
  return a,b
a = 1
b = 9
print(a,b) 


#flexible number of arguments when one does not know the number of arguments
def f2(*args):
  return args
print f2(2),f2(1,2,4,4,5),f2()

def f3(a=144, b=0):
  return a,b
print f3(34)
print f3(b=99)

def f4(*args, **kwords):
  return args,kwords
print f4(1,3,4,5,6,6)

def f5(a,b, *args, **kwds):
  return a,b,args,kwds
print f5(11,19,30,454)



#while True :
#   pass1 = raw_input('Enter password:')
#   pass2 = raw_input('Repeat:')
#   if (pass1 == pass2):
#      break
#   print('Type identical passwords')
#print 'All good'


