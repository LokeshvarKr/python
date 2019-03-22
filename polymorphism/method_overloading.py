class A:
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None :
            s=a+b+c
        elif a!=None and b!=None :
            s=a+b
        else :
            s=a

        return s



a=A()

print(a.sum(4))
print(a.sum(4,5))
print(a.sum(4,5,6))



