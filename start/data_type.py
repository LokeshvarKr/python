print("----------section 1 -----------------")
n=None
a=10
b=20
c=3.5
d='lokesh'
e=2+3j
print("a",a,type(a))
print("b",b,type(b))
print("c",a,type(c))
print("d",d,type(d))
print("e",e,type(e))
print("n",a,type(n))

#conversion
x=int(c)
y=float(b)
z=complex(a,b)

print("x",x,type(x))
print("y",y,type(y))
print("z",z,type(z))
print("b>a",b>a)
print("b<a",b<a)
boolian= b < a
print("boolian",boolian,type(boolian))
print(boolian,int(boolian))
print(b>a,int(b>a))

print("----------section 2 -----------------")
# tuple
# set
# list
# dictionary
# range

l=[2,3,4,5]
t=(34,"sara",4.5,7)
s={8.4,34,122,"lokesh","Kiran"}
r=range(2,10,2)
d={'lokesh':'1234','mithun':'1244','rakesh':'9088','raju':'5678'}
print(l,type(l))
print(t,type(t))
print(s,type(s))
print(r,type(r))
print(d,type(d))

print(r,type(r),list(r),type(list(r)))