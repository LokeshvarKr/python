from array import *
seq=array("i",[int(x) for x in input("Enter array elements: ").split()])

def insert(seq,position):
	x=seq[position]
	while(position>0 and seq[position-1]>x):
		seq[position]=seq[position-1]
		position-=1
	seq[position]=x

def sort(seq,k):
	if(k<2):
		return
	else:
		sort(seq,k-1)
		insert(seq,k-1)

def insertion_sort(seq):
	sort(seq,len(seq))

insertion_sort(seq)
print(seq)

