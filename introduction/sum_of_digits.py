num=input("Enter a number")
n=len(num)
sum=0;
while n > 0:
	x=int(num[n-1])
	sum+=x
	n=n-1;
print("sum is " + str(sum))