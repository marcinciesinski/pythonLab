def euklidesMod(a, b):
  if a <= b:
    return euklidesMod(b, a)
  elif b == 0:
    return a
  else:
    return euklidesMod(b, a % b)

def euklides2(*args):
  return reduce(euklidesMod, args)


print euklides2(9, 6, 12, 99, 30)

print reduce(lambda x,y: x+y,[1,2,3])

print map(lambda x: x+1, [1])