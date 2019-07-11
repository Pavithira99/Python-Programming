n=int(input())
if(n<=3):
  x=list(map(int,input().split(" ")))
x.append(0)
x.append(0)
count=0
for i in range(0,len(x)-2):
  if(x[i]<x[i+1]):
    if(x[i+1]<x[i+2]):
      count+=1
print(count)
