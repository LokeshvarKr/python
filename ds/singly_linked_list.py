from array import  *

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None

    def length(self):
        i=0
        current_node=self.head
        while current_node is not None:
            i+=1
            current_node=current_node.next
        return i


    def insert_as_head(self,node):
        if self.head is None:
            self.head=node
        else:
            temp_node=self.head
            self.head=node
            self.head.next=temp_node
            del temp_node

    def insert(self,node):
        if self.head is None:
            self.head=node
        else:
            last_node=self.head
            while True:
                if last_node.next is None:
                    break
                last_node=last_node.next
            last_node.next=node

    def insert_at_position(self,i,node):
        n=self.length()
        if i < 0 or n < i:
            print(i,"is invalid Index")
            return
        if i is 0 :
            self.insert_as_head(node)
            return
        if i is n :
            self.insert(node)
            return
        j=0
        current_node=self.head
        prev_node=Node
        while True:
            if j == i:
                node.next=current_node
                prev_node.next=node
                break
            j+=1
            prev_node = current_node
            current_node = current_node.next


    ''''
    
    def insert_at_position(self,i,node):
        if i < 0:
            print(i,"is invalid Index")
        if self.head is None and i > 0:
            print(i,"is invalid Index")
            return
        if i is 0:
            temp_node=self.head
            self.head=node
            self.head.next=temp_node
            del temp_node

        current_node =self.head
        j=1
        while current_node.next is not None and j < i:
            current_node=current_node.next
            j+=1;

        if  i > j :
            print(i,"is invalid Index")
        elif current_node.next is None and j is i:
            current_node.next=node
        else:
            next_node=current_node.next
            current_node.next=node
            current_node.next.next=next_node
            del next_node
            del current_node
    
    '''

    def delete_at_postion(self,i):
        if self.head is None:
            print ("List is empty")
            return
        n=self.length()
        if i < 0 or i >=n:
            print (i," is invalid index")
            return

        j=0
        current_node=self.head
        prev_node=None
        while True:
            if j==i:
                break
            j+=1
            prev_node = current_node
            current_node = current_node.next

        if j==0:
            temp_node=self.head
            self.head=current_node.next
            temp_node=None
        else:
            temp_node=current_node
            prev_node.next=current_node.next
            temp_node=None



    def print_list(self):
        if self.head is None:
            print ("List is Empty")
            return
        current_node = self.head
        while True:
            if current_node is None:
                break
            else:
                print(current_node.data,end=' ')
                current_node=current_node.next
        print()


list = linked_list()
a=array('i',[2,3,4,5,6,7,8,9,6,1,2,3,5,7,8,78,35])
#a=array("i",[])

for i in a:
    node=Node(i)
    list.insert(node)

list.print_list()

print ("===============================================")

b=array('i',[1,11,111,12,123,121,21,22,221])

for i in b:
    node=Node(i)
    list.insert_as_head(node)

list.print_list()

print ("================================================")

node=Node(333)
node1=Node(333)
node2=Node(333)

list.insert_at_position(0,node)
list.insert_at_position(list.length(),node1)
list.insert_at_position(12,node2)

list.print_list()
print ("length is ",list.length())

print ("================================================")
print ("Delition section")
list.delete_at_postion(0)
list.print_list()
print ("Length is ",list.length())

list.delete_at_postion(1)
list.print_list()
print ("Length is ",list.length())

list.delete_at_postion(12)
list.print_list()
print ("Length is ",list.length())

list.delete_at_postion(list.length()-1)
list.print_list()
print ("Length is ",list.length())

list.delete_at_postion(list.length())
list.print_list()
print ("Length is ",list.length())
