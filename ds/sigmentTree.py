from array import *

#a=array('i',map(int , input("Enter all array elements").split()))
a=array('i',[int(i) for i in  input("Enter all array elements").split()])

def builtTree(a,tree,s,e,treeNode):
	if s==e:
		tree[treeNode]=a[s]
		return
	else:

		mid=(s+e)/2
		builtTree(a,tree,s,mid,2*treeNode+1)
		builtTree(a,tree,mid+1,e,2*treeNode+2)
		tree[treeNode]=tree[2*treeNode+1]+tree[2*treeNode+2]
		return


tree=array('i',[0 for x in range(3*len(a))])
builtTree(a,tree,0,len(a)-1,0)