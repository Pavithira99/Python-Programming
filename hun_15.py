n=int(input())
x=list(map(int,input().split(" ")))
num=max(x)
num_in=x.index(num)
list1=[]
for i in range(num_in,len(x)):
  list1.appen(x[i])
new=""
new=[str(i) for i in list1]
res=" ".join(new)
print(res)
print(max(x))
