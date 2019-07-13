n=int(input())
arr=list(map(int,input().split()))
arr=[bin(i) for i in arr]
arr.sort(reverse=True)
arr=[int(x,2) for x in arr]

for i in range(0,n):
  print(arr[i])
  
