#!/usr/bin/env python

n = int(raw_input("Which digit?"))

def fib(n):
  if n == 0: return 0
  elif n == 1: return 1
  else: return fib(n-1)+fib(n-2) 
print(fib(n)) 

def nth_fib(n)
  """ Doc """
  prev = 1
  prev_prev = 2
  f_nth = prev
  for i in range(3,n+1):
    f_nth = prev + prev_prev
    #not finished





#while True :
#   pass1 = raw_input('Enter password:')
#   pass2 = raw_input('Repeat:')
#   if (pass1 == pass2):
#      break
#   print('Type identical passwords')
#print 'All good'


