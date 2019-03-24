def max(a, b):
  return a if a>b else b


def higher(*lista, **slownik):
  result = 0;
  if lista:
    result = reduce(max, lista)
    if slownik:
      result = reduce(max, [result] + slownik.values())
    else:
      result = reduce(max, slownik.values())
  return result

print higher("asd", 5, x=2)
