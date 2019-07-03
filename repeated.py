n=int(input())
unique1=[]
arr=list(map(int,input().split(" "))
for i in range(0,len(arr)):
  if(arr.count(i)>1):
    unique1.append(i)
unique1.sort()
new=""
new=[str(i) for i in unique1)
res=" ".join(new)
print(res)
 
