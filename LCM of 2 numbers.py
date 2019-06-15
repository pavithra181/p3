q,p=map(int,input().split())
if(q>p):
    max=q
else:
    max=p
while(1):
    if(max%q==0 and max%p==0):
        print(max)
        break
    max=max+1
