a=[]
x=int(input("Enter the no. of members in list...::  "))
for i in range(0,x) :
    y=int(input())
    a.append(y)
print(a)
y=int(input("\t enter the no. to be searced...::  "))
print("the no. to find is..",y)
if y in a :
   print("\t number is found and deleted ")
   a.remove(y)
else :
   print("number not found")
print(a)
