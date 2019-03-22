from array import  *

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def print_list(head):
    if head is None:
        print("List is Empty")
    else:
        while head is not None:
            print(head.data,end=" ")
            head=head.next

def merge(head1,head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    head=None
    h=None
    while head1 is not None and head2 is not None:
        if head1.data < head2.data:
            if h is None:
                h=head1
                head=head1
            else:
                h.next=head1
                h=h.next
            head1=head1.next
        else:
            if h is None:
                h=head2
                head=head2
            else:
                h.next=head2
                h=h.next
            head2=head2.next

    while head1 is not None:
        h.next = head1
        h = h.next
        head1 = head1.next

    while head2 is not None:
        h.next = head2
        h = h.next
        head2 = head2.next

    return head

def merge_recursively(l1,l2):
    if(l1 is None and l2 is not None):
        return l2
    if(l2 is None and l1 is not None):
        return l1
    node=None
    if(l1.data < l2.data):
        l1.next=merge_recursively(l1.next,l2)
        return l1
    else:
        l2.next=merge_recursively(l1,l2.next)
        return l2


a=array('i',[int(x) for x in input().split()])
b=array('i',[int(x) for x in input().split()])

n=len(a)
m=len(b)

head1=None
head2=None
h1=None
h2=None
i=0
while i < n:
    node=Node(a[i])
    node.next=None

    if h1 is None:
        head1=node
        h1=head1
    else:
        h1.next=node
        h1=h1.next
    i+=1

i=0
while i < m:
    node=Node(b[i])
    node.next=None

    if h2 is None:
        head2=node
        h2=head2
    else:
        h2.next=node
        h2=h2.next
    i+=1

# head=merge(head1,head2)
# print_list(head)
head=merge_recursively(head1,head2)
print_list(head)








