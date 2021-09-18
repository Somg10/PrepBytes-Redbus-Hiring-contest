import math
t = int(input())
while t!=0:
  a,b,c = map(int, input().split())
  r1 = abs(c-a)
  r2 = abs(b-a)
 
  
  if r1 > r2 :
    print("B")
  else:
    print("C")
  t = t-1
