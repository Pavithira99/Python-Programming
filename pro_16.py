n=int(input())
arr=list(map(int,input().split()))
arr.sort()
unique=[]
sum=5
for i in arr:
  if i not in unique:
    unique.append(i)
for i in range(0,len(unique)):
  if(i!=1):
    sum+=(i+1)
print(sum)
