n,m = map(int,input().split())
p= n * m
d = p ** (1/2)
f = d * d
if(f == p):
  print("yes")
else:
  print("no")
