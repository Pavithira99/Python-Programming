n=input()
n=list(n)
x=[]
for i in range(0,len(n),2):
  x.append(n[i+1])
  x.append(n[i])
res="".join(x)
print(res)
