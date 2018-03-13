#!/usr/bin/env python

n = int(raw_input("How long?"))


def gen_f(n):
  i= 0
  while True:
    yield (n-1)+(n+1)

g = gen_f()
  next(g), next(g)

## not finished
