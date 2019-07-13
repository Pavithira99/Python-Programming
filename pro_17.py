n=list(map(int,input().split()))
x=n[1]
arr=list(map(int,input().split()))
arr.append(0)
flag=1
for i in range(0,len(arr)-1):
  if(arr[i]+arr[i+1]==x):
    
    flag=0
    break
if(flag==1):
  print("no")
else:
  print("yes")
