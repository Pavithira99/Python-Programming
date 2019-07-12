n=input().split()
x=list(n[0])
count=0
y=list(n[1])
for i in range(0,len(x)):
  if(x[i]!=y[i]):
    count+=1
if(count==1):
  print("yes")
else:
  print("no")
