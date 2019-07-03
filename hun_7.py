def odd(n):
  if(n%2==0):
    return False
  retuen True
def even(n):
  if(n%2==0):
    return True
  return False
n=int(input())
list1=[]
arr=list(map(int,input().split(" ")))
for i in range(0,n):
  if(odd(i)):
    if(even(arr[i]):
      list1.append(arr[i])
  elif(even(i)):
    if(odd(arr[i]):
      list1.append(arr[i])
new=""
new=[str(i) for i in list1]
res=" ".join(new)
