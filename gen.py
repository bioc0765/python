#!/usr/bin/env python

def gen_sq(n):
  for i in range(n):
    yield i**2

g = gen_sq(6)
for number in g:
  print(number)

