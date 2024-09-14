family=["grandfather","father","mother","brother","sister"]
for x in family:
   print(x)

print("\n-----------string")
for y in "apple":
   print(y)

print("\n-----------break statement")
family=["grandfather","father","mother","brother","sister"]
for x in family:
   print(x)
   if x =="mother":
    break

print("\n----------------")  
for x in family:
   if x =="mother":
    break
   print(x)

print("\n-----------continue statement")
family=["grandfather","father","mother","brother","sister"]
for x in family:
   if x =="mother":
    continue
   print(x)

print("\n-----------range statement")

for x in range(6):
  print(x)
print("\n-----------range statement")
for x in range(2,6):
  print(x)
print("\n-----------range statement")
for x in range(2,30,3):
  print(x)

print("\n-----------range statement")
for x in range(6):
  print(x)
else:
  print("finally finshed")

print("\n-----------range statement")
for x in range(6):
  
  if x==3:break
  print(x)
else:
    print("finally finshed")

print("\n-----------nested for loop statement")
adj=["red","big","testy"]
fruits=["apple","banana","guvava"]
for x in adj:
  for y in fruits:
    print(x,y)

for x in [0,1,2]:
  pass