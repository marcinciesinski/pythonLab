import random
import time
import math
# print ("podaj a")
# a = input()
# print ("podaj b")
# b = input()
def euklidesMod(a, b):
  if a <= b:
    return euklidesMod(b, a)
  elif b == 0:
    return a
  else:
    return euklidesMod(b, a % b)

def euclides(a,b):
  if(a>b):
    while (b!=0):
      c=a%b
      a=b
      b=c
    return a
  else:
    while (a!=0):
      c=b%a
      b=a
      a=c
    return b

def is_prime(num):
  for j in range(2, int(math.sqrt(num)) +1):
    if(num % j) ==0:
      return False
  return True

default_timer = time.time

fst = 10000000000L
snd = 10000010000L

start = default_timer()

big3 = filter(is_prime, range(fst, snd))

stop = default_timer()

print 'Time is_prime:', stop - start

prime = 0

start = default_timer()
for prime in big3:
    euclides(prime * prime, prime * prime * prime)
stop = default_timer()
print 'Time euklides:', (stop - start) * 1000

start = default_timer()
for prime in big3:
    euklidesMod(prime * prime, prime * prime * prime)
stop = default_timer()
print 'Time euklidesMod:', (stop - start) * 1000
#
# print (euclides(a,b))