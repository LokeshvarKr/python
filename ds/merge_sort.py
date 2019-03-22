from array import *
def merge(a,p,q,r):
	a1=array('i',[x for x in a[p:q+1]])
	a2=array('i',[x for x in a[q+1:r+1]])
	(n1,n2)=(len(a1),len(a2))
	(i,j,k)=(0,0,p)
	while(i<n1 and j<n2):
		if(a1[i]<a2[j]):
			a[k]=a1[i];
			(i,k)=(i+1,k+1)
		else:
			a[k]=a2[j];
			(j,k)=(j+1,k+1)

	while(i<n1):
		a[k]=a1[i]
		(i,k)=(i+1,k+1)
	while(j<n2):
		a[k]=a2[j]
		(j,k)=(j+1,k+1)


def  mergesort(a,p,r):
	if(p<r):
		q=p+(r-p)//2
		mergesort(a,p,q)
		mergesort(a,q+1,r)
		merge(a,p,q,r);


a=array('i',[int(x) for x in input("Enter Elements: ").split(' ')])
mergesort(a,0,len(a)-1)
print(a)