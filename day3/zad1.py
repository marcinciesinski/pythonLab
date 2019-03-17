print ("podaj a")
a = input()
print ("podaj b")
b = input()

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
print (euclides(a,b))