from numpy import *
print('============2d==========')
num=array([
	[2,3,4,5,6],
	[3,3,4,3,2],
	[3,4,5,6,7]
	])
print(num)
print(num.ndim)
print(num.shape)
print(num.size)

new_num=num.flatten()
print(new_num)


print('============3d==========')

#in 2d
arr=num.reshape(5,3)
print(arr)
#in 3d
arr=num.reshape(3,1,5)
print(arr)


