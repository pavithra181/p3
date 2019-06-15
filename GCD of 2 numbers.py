p,t=map(int,input().split())
i=1
while(i<=p and i<=t):
  if(p%i==0 and t%i==0):
    gcd=i
  i=i+1
print(gcd)
