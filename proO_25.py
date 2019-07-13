nnn=int(input())
xxx=list(map(int,input().split(" ")))
list1=[]
for i in xxx:
  list1.append(xxx.count(i))
print(max(list1))
