p = int(input())
if(p>1):
  for j in range(2,p):
    if (p%j==0):
      print ("yes")
      break
  else:
    print ("no")
else:
  print ("no")
