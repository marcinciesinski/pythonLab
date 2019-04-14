import math

class Punkt:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def odleglosc(self, p):
    return math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)

  def przesunX(self,w):
    return self.x += w

  def przesunY(self,w):
    return self.y += w
  
  def __setitem__(self, key, value):
    if(key == 'x'):
      self.x = value
    elif(key == 'y'):
      self.y = value

  def __getitem__(self, key):
    if(key == 'x'):
      return self.x
    elif(key == 'y'):
      return self.y


class Prostokat:
  def __init__(self, punkt, odlegloscX, odlegloscY):
    pass #dokonczyc sobie pozniej
