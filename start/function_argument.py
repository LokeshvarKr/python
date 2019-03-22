
def update(x):
	print(id(x))
	print("x",x)
	x=8
	print(id(x))
	print("x",x)

def update_list(l):
	print(id(l))
	print("l",l)
	l[1]=10
	print(id(l))
	print("l",l)

a=10
print(id(a))
print("a",a)
# in python we don't have pass by value,reference condepts
# because these int,str ,...etc all are objects in python
# and are immutable 
update(a)
print("a",a)


lst=[2,3,5,6]
print(id(lst))
print(lst)
# here its change the original value too because 
# list is mutable
update_list(lst) 

print("---------------------------")
def person(name,age):
	print(name)
	print(age-5)

person(age=28,name="lokesh")
# this will give error--> person(28,"lokesh")
person("lokesh",25)



print("---------------------------")
# by default argument
def person1(name,age=18):
	print(name)
	print(age)

person1(name="lokesh")
# this will give error--> person(28,"lokesh")
person1("lokesh")



print("---------------------------")
# variable length argument
# here b will be tuple
'''
def sum(a,*b):
	print(a)
	print(b)
	c=a;
	
	for i in b:
		c=c+i

	print(c)
'''
def sum(*b):
	print(a)
	print(b)
	c=0;
	
	for i in b:
		c=c+i

	print(c)

sum(8,6,6,7,7,8,9)

print("---------------------------")
#keyword variable length argument
def person2(name,**data):
	print(name)
	print(data)

	for i , j in data.items():
		print(i,j)


person2('lokesn',age=29,city='mumbai',mob=8929328292)

