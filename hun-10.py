n=list(map(int,input().split(" ")))
arr1=list(map(int,input().split(" ")))
flag=0
arr2=list(map(int,input().split(" ")))
for i in arr2:
  if(i not in arr1):
    print("NO")
    break
  else:
    flag=1
 if(flag==1):
  print("YES")
   
