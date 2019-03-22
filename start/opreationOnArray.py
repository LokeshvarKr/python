from numpy import *

print("-------operations---------------")
print(".......... num=num+5 ...........")

num=array([2,3,4,5,6])
num=num+5;
print(num)
print()


print(".. addNum=num+new_num ..")
new_num=array([1,1,1,2,4])
addNum=num+new_num;
print("num",num)
print("new_num",new_num)
print("addNum",addNum)
print()

print("..... sin(num),cos(num)..............")
print(sin(num))
print(cos(num))
print()

print("........  log(num) ...............")
print(log(num))
print()

print("............ sqrt(num) ............")
print(num)
print(sqrt(num))
print()

print("............ sum(num) ............")
print(num)
print(sum(num))
print()

print("............ concatinate([num,new_num]) ............")
print(concatenate([addNum,new_num]))
print()
print(num)
print(new_num)
print(addNum)