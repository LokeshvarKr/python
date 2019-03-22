class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=None

    def print_list(self):
        if self.head is None:
            print("List is Empty")
        else:
            h=self.head
            while h:
                print(h.data,end=" ")
                h=h.next
            print()
        return

    def insert_as_head(self,node):
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

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

    def __reverse_in_pair_recursively(self,node):
        if node is None or node.next is None:
            return node
        else:
            n1=node
            n2=node.next
            node=node.next.next
            n1.next=None
            n1.next=self.__reverse_in_pair_recursively(node)
            n2.next=n1
            return n2

    def __reverse_in_pair_iteratively(self,node):
        if node is None or node.next is None:
            return node
        else:
            prev=None
            h=None
            while(node is not None and node.next is not None):
                n1 = node
                n2 = node.next
                node = node.next.next
                n1.next=None
                n2.next = n1
                if h is None:
                    h=n2
                    prev=n1
                else:
                    prev.next=n2
                    prev=n1

            if node is not None:
                prev.next=node
            return h

    def reverse_in_pair(self):
        # all node we have inserted as head so first
        # of all we need to reverse this linked_list
        self.head=self.__reverse_iteratively(self.head)
        # then reverse in pair
        self.head=self.__reverse_in_pair_recursively(self.head)
        self.print_list()
        self.head=self.__reverse_in_pair_iteratively(self.head)
        self.print_list()


a=[int(e) for e in input().strip().split()]
list=linked_list()
for e in a:
    node=Node(e)
    list.insert_as_head(node)

# list.print_list()
list.reverse_in_pair()
