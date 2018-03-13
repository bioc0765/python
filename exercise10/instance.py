#/usr/bin/env python

class Vector:
  def set_coordinates(self, *coordinates):
      self.coordinates = coordinates
  def compute_length(self):
      return sum([abs(_) for _ in self.coordinates])
