n=list(map(str,input().split(" ")))

for i in n:
  list1.append(i.reverse())
new=""
new=[str(i) for i in list1]
res=" ".join(new)
