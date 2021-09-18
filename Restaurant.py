import math
t = int(input())
while t!=0:
  sm = 0
  n = int(input())
  a = list(map(int, input().split(' ')[:n]))
  for i in range (n):
    sm = sm + a[i]

  print(int(math.ceil(sm/2)))
  t = t-1
