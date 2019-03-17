def euklidesMod(a, b):
  if a <= b:
    return euklidesMod(b, a)
  elif b == 0:
    return a
  else:
    return euklidesMod(b, a % b)

def is_prime(num):
  for j in range(2, int(math.sqrt(num)) +1):
    if(num % j) ==0:
      return False
  return True

