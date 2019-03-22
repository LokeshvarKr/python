#code
from math import gcd
from array import array


# method 1
# time=o(n) space = o(1) 
def reverseArray(a,n,d):
    g=gcd(d,n)
    for i in range(0,g):
        j=i
        temp=a[i]
        while(1):
            k=(j+d)%n
            if(k==i):
                break
            a[j]=a[k]
            j=k
        
        a[j]=temp
    
t=int(input())
while t:
    t-=1
    n,d=input().split()
    (n,d)=(int(n),int(d))
    a=array('i',[int(x) for x in input().split()]);
    reverseArray(a,n,d)
    for e in a:
        print(e,end=" ")
    print()
    


'''
#methd 2
# time complexity=o(d+(n-d)+n)=o(2n) space =o(1)
def reverse(a,s,e):
    (i,j)=(s,e)
    while(i<=j):
        (a[i],a[j])=(a[j],a[i])
        (i,j)=(i+1,j-1)

t=int(input())
while t:
    t-=1
    n,d=input().split()
    (n,d)=(int(n),int(d))
    a=array('i',[int(x) for x in input().split()]);
    reverse(a,0,d-1);
    reverse(a,d,n-1);
    reverse(a,0,n-1);
    for e in a:
        print(e,end=" ")
    print()
    
'''


