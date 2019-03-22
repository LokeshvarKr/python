def add(a,b):
	return a+b

def multply(a,b):
	return a*b

def divide(a,b):
	if b!=0:
		return a/b
	else:
		return -1

def subtract(a,b):
	return a-b

def fact(n):
	result=1
	for i in range(1,n+1):
		result*=i
	return result;

def square(a):
	return a*a

def cube(a):
	return a*a*a

def power(a,b):
	return a**b
