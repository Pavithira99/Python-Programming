n=list(map(str,input().split(" ")))
li=[]
for i in n:
  li.append(i[::-1])

res=" ".join(li)
