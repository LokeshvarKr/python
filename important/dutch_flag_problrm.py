from array import *
a=array('i',[int(x) for x in input(" enter array elements: ").split(' ')])
print (a)

# dutch national problem
low=0
mid=0
high=len(a)-1
while(mid<=high):
	if(a[mid]==0):
		a[low],a[mid]=a[mid],a[low]
		low+=1
		mid+=1
	elif(a[mid]==1):
		mid+=1
	elif(a[mid]==2):
		a[mid],a[high]=a[high],a[mid]
		high-=1
	else:
		pass


print(a)
