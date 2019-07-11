n=input()
list1=[]
for i in n:
  list1.append(int(i))
list1.sort()
new=""
new=[str(i) for i in list1]
res="".join(new)
