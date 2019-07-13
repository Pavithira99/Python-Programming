n=int(input())
list1=[]
list2=[]
for i in range(0,n):
  list1.append("{}")
for i in range(0,n):
  list2.append("{")
for i in range(0,n):
  list2.append("}")
new=""
res="".join(list1)
print(res)
res="".join(list2)
print(res)
