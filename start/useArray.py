# to import everything from array module 
# need to use * and write as below
# from array import * 


# import array from module array
from array import array


num=array('i',[2,3,2,5,6,7,8])

print("---------------------------")

print(num)
print(num.buffer_info())
print(num.typecode)
num.reverse()
print(num)


print("---------------------------")

for i in range(len(num)) :
	print(num[i],end=" ")
print()

squareNum=array(num.typecode,(a*a for a in num))
for v in squareNum :
	print(v,end=" ")
print()

print("-----------------------------")
newArray=array('i',[])
n=int(input("Enter size of array u want : "))
for i in range(n):
	x=int(input("Enter an element of array : "))
	newArray.append(x)


x=int(input("Enter an element u want to search form this array : "))

# manually
i=0;
for e in newArray:
	if e==x:
		print("prensent at index " + str(i))
		break
	i+=1


for i in range(len(newArray)) :
	if newArray[i]==x :
		print("prensent at index " + str(i))
		break


print("prensent at index", newArray.index(x))

from numpy import *
num=array([4,4,4,3,2,2,6,5.6,5.6])