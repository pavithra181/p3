p=list(input())
b=len(p)
if(b%2==1):
	c=b//2
	p[c]='*'
	print("".join(p))
elif(b%2==0):
	c=b//2
	p[c]=p[c-1]='*'
	print("".join(p))
