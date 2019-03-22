from numpy import *
print("-------------------------")
num=array([
	[2,3,4,5,6],
	[3,3,4,3,2],
	[3,4,5,6,7]
	])
m=matrix(num)
print(m)

print("-------------------------")
m=matrix('1 2 ; 2 4 ; 5 7; 4 6')
print(m)

print("-------------------------")
m=matrix('1 2  2; 4  5 7; 4 6 9')
print(m)
print()
print(diagonal(m))
print()
print(m.min())
print()
print(m.max())

print("-------------------------")
m1=matrix('1 6 2; 4 7 7; 4 1 9')
m2=matrix('1 2 2; 4 5 1; 4 6 1')
m=m1*m2;
print("m1*m2",m)

