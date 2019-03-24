
cennik = {"chleb": 2.5, "mleko": 3, "papier": 7.40, "platki": 3.50}

lista = ["mleko","chleb","platki"]


def zakupy(cennik, lista):
  spis = {}
  for l in lista:
    if l in cennik:
      spis[l] = cennik[l]
  return spis

print zakupy(cennik,lista)
