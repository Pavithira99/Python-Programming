n=int(input())
list1=[]
arr=list(map(int,input().split(" ")))
for i in range(0,len(arr)):
  if(i==arr[i]):
    list1.append(i)
new=""
new=[str(i)for i in list1]
res=" ".join(new)
