from array import *
a=array('i',[int(x) for x in input("Enter array elements: ").split()])
n=len(a)
for i in range(1,n):
	j=i-1
	x=a[i]
	while j >= 0 and a[j] > x:
			a[j+1]=a[j];
			j-=1
	a[j+1]=x
	
print(a)