n=list(map(int,input().split(" ")))
arr=list(map(int,input().split(" ")))
list1=[]
x=arr.index(n[1])
list1.append(arr[x-1])
list1.append(arr[x+1])
if(arr[x-2]>arr[x+2]):
  list1.append(arr[x+2])
else:
  list1.append(arr[x+1])
new=""
new=[str(i) for i in list1]
res=" ".join(new)
print(res)
  
