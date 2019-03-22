from numpy import *

num=array([2,3,4,5,6])
print("-----------------------------")
#num and new_num both are same , new_num is just alias of num
#both has same address
new_num=num;
print(num)
print(new_num)
print(id(num))
print(id(new_num))


print("-----------------------------")
# to create two different array with same value 
# we use view() method
# but this is shallow copy
new_num=num.view()
print(num)
print(new_num)
print(id(num))
print(id(new_num))

num[1]=7
#now in both array change will reflect
print(num)
print(new_num)


print("-----------------------------")
# for deep copy use copy()
new_num=num.copy()
print(num)
print(new_num)
print(id(num))
print(id(new_num))

num[0]=5
#now change will reflect in num only
print(num)
print(new_num)


print("-----------------------------")
arr=array([[2,3,4],[3,5,6]],int)
print(arr)
print()

arr=array(['a','b','c','d'],str)
print(arr)
print()
arr=array([3.4,5.6,6.7],float)
print(arr)
print()
