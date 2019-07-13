nn=int(input())
xx=list(map(int,input().split(" ")))
list1=[]
for i in xx:
  list1.append(xx.count(i))
print(max(list1))
