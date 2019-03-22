import sys

sys.setrecursionlimit(100000)
#Euclid algorithm recursive

def gcd1(a,b):
    if a==0:
        return b
    if b==0:
        return a
    # now make a > b
    if a < b:
        a,b=b,a

    if a%b == 0:
        return b
    return gcd1(b,a-b)

def gcd2(a,b):
    if a is None:
        return b
    if b is None:
        return a

    # now make a > b
    if a < b:
        a,b=b,a

    if a%b == 0:
        return b
    return gcd2(b,a%b)

#Euclid algorithm iterative
def gcd3(a,b):
    if a is None:
        return b
    if b is None:
        return a

    # now make a > b
    if a < b:
        a,b=b,a
    '''
    while b!=0:
        x=a%b
        a=b
        b=x
    return a
    '''
    while a%b!=0:
    	a,b=b,a%b
    
    return b


def gcd4(a,b):
    if a is None:
        return b
    if b is None:
        return a

    # now make a > b
    if a < b:
        a,b=b,a

    while b!=0:
        a=a-b
        if(a < b):
            a,b=b,a
    return a


print (gcd1(21,0))
print (gcd2(21,0))
print (gcd3(21,0))
print (gcd4(21,0))
