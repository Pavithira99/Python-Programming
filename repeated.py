n=int(input())
unique=[]
arr=list(map(int,input().split(" "))
for i in range(0,len(arr)):
  if(arr.count(i)>1):
    unique.append(i)
unique.sort()
new=""
new=[str(i) for i in unique)
res=" ".join(new)
print(res)
 
