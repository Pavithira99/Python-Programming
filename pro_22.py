n=int(input())
arr=list(map(int,input().split()))
sum=0
list1=[]
for i in range(0,len(arr),2):
  sum+=arr[i]
  list1.append(sum)
sum=0
for i in range(1,len(arr),2):
  sum+=arr[i]
  list1.append(sum)
print(max(list1))
