n=list(map(int,input().split(" ")))
count=0
arr=list(map(int,input().split(" ")))

for i in range(0,n[0]):
  count+=1
  x=max(arr)
  if(count==n[1]):
    print(x)
    break
  else:
    arr.remove(x)
