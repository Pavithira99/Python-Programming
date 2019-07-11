n=input().split(" ")
l1=list(n[0])
l2=list(n[1])
x=len(n[0])
y=len(n[1])
f=0
if(x<y):
  for i in range(0,x):
    if(l1[i]==l2[i]):
      continue
    else:
      f=i+1
      break
  print(y-f)
else:
  for i in range(0,y):
    if(l1[i]==l2[i]):
      continue
    else:
      f=i+1
      break
  print(x-f)
  


