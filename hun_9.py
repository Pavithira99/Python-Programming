n=int(input())
arr=list(map(int,input().split(" ")))
list1=[]
for i in range(n):
  for j in range(n):
    if(i!=j):
      if(arr[i]+arr[j]==0):
        list1.append(arr[i])
        list1.append(arr[j])
        break
new=""
new=[str(i) for i in list1]
res=" ".join(new)
