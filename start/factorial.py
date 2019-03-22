
n=int(input())

def fact_iterative(n):
	result=1
	for i in range(1,n+1):
		result*=i
	return result

result=fact_iterative(n)
print("n! :",result)


# in python by default maximum recursion depth is 1000
def fact(n):
	if(n==1):
		return 1
	return n*fact(n-1)

result=fact(n);
print("{}! : {}".format(n,result))