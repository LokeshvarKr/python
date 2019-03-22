
def greet():
	print("hello")
	print("Good morning")

def add(a,b):
	c=a+b
	print(c)

def addd(x,y):
	return x+y

def add_sub(x,y):
	z=x+y
	w=x-y
	return z,w	

greet()
greet()

add(4,5)
add(77777777,111111111)
add(892.949343,9343.23434)

x=addd(4,5)
print(x)
x=addd(77777777,111111111)
print(x)
x=addd(892.949343,9343.23434)
print(x)

a,b=add_sub(4,5)
print(a,b)
a,b=add_sub(77777777,111111111)
print(a,b)
a,b=add_sub(892.949343,9343.23434)
print(a,b)

