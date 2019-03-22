from array import *

a=array('i',[int(x) for x in input("Enter array elements : ").split()])

#selection sort
n=len(a)
for i in range(n):
	minm=i
	for j in range(i,n):
		if a[j] < a[minm]:
			minm=j

	a[i],a[minm]=a[minm],a[i]


print(a)
