n=input()
v=['a','e','i','o','u']
if(not n.isalnum()):
  print("Invalid")
elif(n in v):
  print("Vowel")
else:
  print("Consonant")
