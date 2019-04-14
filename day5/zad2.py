class Zwierz:
  def reply(self):
    return self.glos()

class Ssak(Zwierz):
  def glos(self):
    return "Ssak: glos"


class Kot(Ssak):
  def glos(self):
    return "Mial !"


class Pies(Ssak):
  def glos(self):
    return "Hau Hau !"


class SsakNaczelny(Ssak):
  def glos(self):
    return "Witaj !"


class Haker(SsakNaczelny):
  pass

