print("--------------while loop----------------")

i=1
while i<=10:
	print("hello!")
	i=i+1;
i=0
x=0
while i<10**6:
	x+=10
	i=i+1

print(x)

print("-------------------for loop--------------")
for var in range(10):
	print("hello!")
print("-----------------------------------------")
for var in range(10):
	print("var value is : ", end="" )
	print(var)
print("-----------------------------------------")
for var in range(50,100):
	if(var >= 60):
		break;
	if(var%2==0):
		continue
	print("var value is : ", end="" )
	print(var)

print("-----------step in for loop--------------")
# using step argument in for loop (start,stop,step)
for var in range(50,100,10):
	print("var value is : ", end="" )
	print(var)
print("-----------------------------------------")
for var in range(10,-1,-1):
	print("var value is : ", end="" )
	print(var)
print("---------------------end-----------------")










