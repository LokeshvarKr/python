class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None

    def insert_as_head(self,node):
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def print_list(self):
        if(self.head is None):
            print("List is Empty")
            return
        h=self.head
        while True:
            if h is None:
                break
            else:
                print(h.data,end=' ')
                h=h.next
        print()

    def __reverse_recursively(self,node):
        if(node is None or node.next is None):
            return node
        nextNode=node.next
        node.next=None
        reversedList=self.__reverse_recursively(nextNode)
        nextNode.next=node
        return reversedList
    def __reverse_iteratively(self,h):
        if(h is None or h.next is None):
            return h
        prev,curr,next=None,h,None
        while(curr is not None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev
    def reverse_linked_list(self):
        self.head=self.__reverse_recursively(self.head)
        self.print_list()
        self.head=self.__reverse_iteratively(self.head)
        self.print_list()



list=linked_list()
a=[1,2,3,4,5,6,7]
for e in a:
    node=Node(e)
    list.insert_as_head(node)
list.print_list()
list.reverse_linked_list()
# list.print_list()