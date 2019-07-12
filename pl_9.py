def prime(n):
  for i in range(2,n):
    if(n%i==0):
      return False
    return True
n=list(map(int,input().split(" ")))
list1=[]
for i in range(n[0],n[1]):
  if(prime(i)):
    list1.append(i):
new=""
new=[str(i) for i in list1]
res=" ".join(new)
print(res)
