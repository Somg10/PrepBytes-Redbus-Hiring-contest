import math
n=int(input())
A=list(map(int,input().split()))
a_min=min(A)
x=dict()
for a in A:
    for i in range(1,int(a**0.5)+1):
        if i>=a_min: break
        if a%i==0:
            if i in x:
                x[i]=math.gcd(x[i],a)
            else:
                x[i]=a
            j=a//i
            if j>=a_min: continue
            if j in x:
                x[j]=math.gcd(x[j],a)
            else:
                x[j]=a
ans=1
for k in x.keys():
    if k==x[k]:
        ans+=1
print(ans)   
  
