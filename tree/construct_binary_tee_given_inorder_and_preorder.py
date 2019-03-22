
class node:
    def __init__(self,data):
        self.data=data;
        self.left=None;
        self.right=None;


def print_post_order(root):
	if root is None:
		return
	print_post_order(root.left)
	print_post_order(root.right)
	print(root.data)

def search(arr,start,end,data):
	for i in range(start,end+1):
		if arr[i]==data:
			return i

pre_order_index=0
def construct_binary_tree(pre_order,in_order,in_order_start,in_order_end):
	global pre_order_index
	
	if in_order_start > in_order_end:
		return None
	
	newNode=node(pre_order[pre_order_index])
	pre_order_index+=1
	
	if in_order_start == in_order_end:
		return newNode
	in_order_index=search(in_order,in_order_start,in_order_end,newNode.data)
	newNode.left=construct_binary_tree(pre_order,in_order,in_order_start,in_order_index-1)
	newNode.right=construct_binary_tree(pre_order,in_order,in_order_index+1,in_order_end)
	return newNode


pre_order=[1,2,4,5,8,3,6,9,10,7];
in_order=[4,2,8,5,1,6,10,9,3,7];
root=construct_binary_tree(pre_order,in_order,0,9)
print_post_order(root)
