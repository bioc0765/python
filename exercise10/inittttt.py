#/usr/bin/env python

## incomplete

class Person:
  def __init__(self,name, age, *coordinates):
      self.name = name
      self.age = age
      self.coordinates = coordinates
  def say_hello(self):
      print("hello", self.name)
      return sum([abs(_) for _ in self.coordinates])
  def set_coordinates(self, *coordinates):
      self.coordinates = coordinates
  def compute_length(self):

wan = Person("wan", 96, 1000, 2000, 30000)
wan.say_hello()

