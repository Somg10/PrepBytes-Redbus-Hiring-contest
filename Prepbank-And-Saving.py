t = int(input())
while t!=0:
t = int(input())
while t!=0:
  n = int(input())
  if n == 1:
    print(1)
  else:
    i=1
    sum=0
    while sum < n :
      sum = sum + i
      i = i+1
    print(i-1)
  t = t - 1
