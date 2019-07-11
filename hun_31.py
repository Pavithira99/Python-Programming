prod=1
n=int(input())
x=list(map(int,input().split(" ")))
for i in x:
  prod*=i
print(abs(prod))
