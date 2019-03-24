

w1 = (1,2,3,4)
w2 = (4,6,3,4)

def scalar(w1, w2):
  s=0
  for i in range(0, len(w1)):
    s= w1[i] * w2[i]
  return s


#print [w1[i] for i in range(len(w1)) if w1[i] % 2 == 0]
#print [w1[i] + w2[i] for i in range(len(w1)) if w1[i] % 2 == 0]
print map((lambda x, y: x+y), w1, w2)

#print reduce((lambda x,y: x+y), map((lambda x,y: x*y), w1, w2))
