n=input()
v=['a','e','i','o','u','A','E','I','O','U']
if(not n.isalnum()):
  print("Invalid")
elif(n in v):
  print("Vowel")
else:
  print("Consonant")
