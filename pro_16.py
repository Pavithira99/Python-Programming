n=int(input())
arr=list(map(int,input().split()))
for i in range(0,n):
  print(max(arr))
  arr.remove(max(arr))
  
