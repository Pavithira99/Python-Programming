n=list(map(int,input().split()))
arr=list(map(int,input().split()))
list1=[]
list2=[]
for i in range(0,n[1]):
  x=list(map(int,input().split()))
  list1.append(x[0])
  list2.append(x[1])
for i in range(0,len(list1)):
  sum=0
  new_list=[]
  for j in range(list1[i-1],list2[i]):
    new_list.append(arr[j])
  print(min(new_list))
