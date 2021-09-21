import math


def findMaxGCD(arr, n) :
  high = 0
	i = 0
	while i < n :
		high = max(high, arr[i])
		i = i + 1
    divisors = [0] * (high + 1)
    i = 0
	while i < n :
    j = 1
		while j <= math.sqrt(arr[i]) :
      if (arr[i] % j == 0) :
        divisors[j]= divisors[j]+1
        if (j != arr[i] / j) :
          divisors[arr[i] // j] = divisors[arr[i] // j]+ 1
			
			j = j + 1
      i = i + 1		
	i = high
	while i >= 1 :if (divisors[i] > 1) :
			return i
		i = i - 1
	return 1
	
	
t = int(input())
while t!=0:
    x,y = map(int, input().split())
    arr =[]
    l=y-x
    n = l+1
    for i in range(0,n):
        z = x+i
        arr.append(z)
    #r = n-1
    gh = findMaxGCD(arr,n)
    print(gh)
    t=t-1    
