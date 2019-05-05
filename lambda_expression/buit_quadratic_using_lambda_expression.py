

def build_quadratic_function(a,b,c):
	# returns the function f(x) = ax^2 + bx + c
	return lambda x:a*(x**2)+b*x+c


#############################################

f=build_quadratic_function(2,3,4)

#and then use this quadratic function

print("f(0) : ",f(0))
print("f(1) : ",f(1))

##############################################

print("==================================")
# another way 
# Note : below code is not most redable so sometime its totally fine to write few lines more code

print(build_quadratic_function(2,3,4)(0))
print(build_quadratic_function(2,3,4)(1))
print(build_quadratic_function(1,2,3)(0))
print(build_quadratic_function(3,0,-1)(0))

