
print("-----------------------------------")
a=5
b=6

print(a+b) # + --------> int.__add__(a,b)
print(int.__add__(a,b))

print(a-b) # - ---->  int__sub__(a,b)
print(int.__sub__(a,b))

print(a) #  ------> int.__add__(a,b)
print(int.__str__(a))

print(a>b)
print(int.__gt__(a,b))

print(a<b)
print(int.__lt__(a,b))

print("-----------------------------------")
# now let work on operator overloading

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self, other):
        m1=self.m1 + other.m1
        m2=self.m2 + other.m2
        s=student(m1,m2)
        return s

    def __gt__(self, other):
        x=self.m1 + self.m2
        y=other.m2 + other.m2
        return x>y


    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)



print("-----------------------------------")
raju=student(56,78)
ranjeet=student(82,93)
rakesh=student(43,34)

s1=raju+rakesh
print(s1.m1,s1.m2)
# or
print(s1) # ------> __str__(s)

if raju > rakesh :
    print("raju win")
else:
    print("rakesh win")

if(ranjeet < raju):
    print("ranjeet loose")
else:
    print("raju loose")

print("-----------------------------------")
