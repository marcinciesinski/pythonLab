__name__

def liczbaLini(nazwa_pl):
  file = open (nazwa_pl)
  lines = file.readlines()
  print len(lines)

def liczbaZnakow(nazwa_pl):
  file = open(nazwa_pl)
  chars = len(file.read())
  print chars

def test(nazwa_pl):
  print __name__
  liczbaLini(nazwa_pl)
  liczbaZnakow(nazwa_pl)

if __name__ ==  "__main__":
  test()
