

# lambda is keword used to indicate lambda expression or anonymous function 


print("========================")

#quadratic equation
f=lambda x: 2*(x**2) + 3*x - 4 

print("f(1)",f(1))
print("f(2)",f(2))
print("f(3)",f(3))
print("f(4)",f(4))

print("=======================")

#geometric mean
g=lambda x,y: (x*y)**0.5

#harmonic mean
h=lambda x,y,z: 3/(1/x+1/y+1/z)


print("g(4,9) : ",g(4,9))
print("h(1,2,3) : ",h(1,2,3))

print("=======================")
