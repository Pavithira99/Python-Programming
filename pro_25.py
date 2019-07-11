n=int(input())
x=list(map(int,input().split(" ")))
list1=[]
for i in x:
  list1.append(x.count(i))
print(max(list1)
