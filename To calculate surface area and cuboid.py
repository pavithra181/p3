p,o,b=map(int,input().split())
volume=p*o*b
surfacearea=2*(p*o+o*b+b*p)
print(surfacearea,volume,end=" ")
