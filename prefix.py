n=int(input())
list1=[]
for i in range(n):
  x=input()
  list1.append(x)
val=list1[0]
length=len(val)
for i in range(1,len(list1)):
  if(val in list1[i]):
    continue
  else:
    
    val=val[:length-1]
    length-=1
print(val)
    
    
  
  
