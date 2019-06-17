g,h=map(int,input().split())
l1=list(map(int,input().split()))
for i in range(0,g):
	if(i==h):
		print(l1[i-1])
