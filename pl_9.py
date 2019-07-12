def prime(n):
  for i in range(2,n):
    if(n%i==0):
      return False
    return True
count=0
n=list(map(int,input().split(" ")))
list1=[]
for i in range(n[0],n[1]):
  if(prime(i)):
    count+=1
print(count)
