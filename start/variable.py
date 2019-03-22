print("-----------------")
num=1000;
print(num);
print(id(num))# for address of num
name="lokesh"
print(name)
print(id(name))
print("-----------------")
a=10;
b=a;
print("a",a,id(a))
print("b",b,id(b))
print("10",10,id(10))

k=9;
print("k",k,id(k))
k=10;
print("k",k,id(k))
a=9;
print("a",a,id(a))
b=8;
print("b",b,id(b))

# there is no constant values in python
# but we can give intuition using capital letters variable
# here i'm just trying to indicate that PI is constant 
#(but actually its not as it is only a simple variable ) 
PI=3.14

# types 
print(type(PI))
print(type(a))
print(type(name))
