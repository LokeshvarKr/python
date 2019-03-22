from array import *

def binary_search(seq,l,r,val):
	if (r-l==0):
		return False
	mid=l+(r-l)//2
	if(val==seq[mid]):
		return True
	if(val < seq[mid]):
		return binary_search(seq,l,mid-1,val)
	else:
		return binary_search(seq,mid+1,r,val)


a=array('i',[int(x) for x in input("Enter elements: ").split()])
val=int(input("Enter value to be search: "))
print(binary_search(a,0,len(a)-1,val))
