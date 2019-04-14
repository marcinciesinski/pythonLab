

class Sum:
  def dodaj(self, x):
    self.pole = 1
    print "brak implementacji"
  def __str__(self):
    return str(self.pole)

class ListSum(Sum):
  def __init__(self, l=[]):
    self.pole = l
  def dodaj(self, x):
    self.pole += x.pole
    return self

class SlowSum(Sum):
  def __init__(self, l={}):
    self.pole = l
  def dodaj(self, x):
    self.pole.update(x.pole)
    return self


a = ListSum([1, 2, 3])
b = ListSum(["a", "b", "c"])

print a.dodaj(b)

x = SlowSum({1:'a'})
y = SlowSum({2:'b'})

print x.dodaj(y)

asd = ListSum([5,6,7])
print asd.dodaj([7,8,9])