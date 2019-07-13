k=int(input())
list1=[]
sum=[]
for i in range(0,k):
  x=list(map(int,input().split()))
  list1.append(x)
for i in list1:
  sum+=i
sum.sort()
new=""
new=[str(i) for i in sum]
res=" ".join(new)
print(res)
