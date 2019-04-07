

class Sum:
  def dodaj(self, x, y):
    print "brak implementacji"

class ListSum:
  def dodaj(self, *x, *y):
    print self.x + self.y

class SlowSum:
  def dodaj(self, **x, **y):
    new = self.x.values() + self.y.values()
    print new


a = Sum()
a.dodaj(5, 6)
