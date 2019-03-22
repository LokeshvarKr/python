import sys
# in python by default maximum recursion limit is 1000
print(sys.getrecursionlimit())

# but we can set recursion limit
sys.setrecursionlimit(100000000)
print(sys.getrecursionlimit())

n=int(input("Enter value of n :"))

def fact(n):
	if(n==1):
		return 1
	return n*fact(n-1)


result=fact(n);
print("{}! : {}".format(n,result))