n=list(map(str,input().split(" ")))
list1=[]
for i in n:
  list1.append(i[::-1])
new=""
new=[str(i) for i in list1]
res=" ".join(new)
