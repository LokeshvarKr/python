from array import *
from random import *

def partition(a,p,r):
	pivot=randint(p,r)
	(a[pivot],a[r])=(a[r],a[pivot])
	i=p-1;
	for j in range(p,r):
		if(a[j]<a[r]):
			i=i+1
			(a[i],a[j])=(a[j],a[i])

	i=i+1
	(a[i],a[r])=(a[r],a[i])
	return i


def quicksort(a,p,r):
	if(p<r):
		q=partition(a,p,r);
		quicksort(a,p,q-1);
		quicksort(a,q+1,r);

a=array('i',[int(x) for x in input("Enter Elements: ").split(' ')])
quicksort(a,0,len(a)-1)
print(a)