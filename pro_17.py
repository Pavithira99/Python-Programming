n=list(map(int,input().split()))
arr=list(map(int,input().split()))
flag=1
for i in range(0,n[0]):
  if(arr[i]+arr[i+1]==n[1]):
    print("yes")
    flag=0
    break
if(flag==1):
  print("no")
