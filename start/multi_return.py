lst=[3,4,5,6,4,33,5,2]
def count(lst):
	even=0
	odd=0
	for i in lst:
		if i%2==0:
			even+=1
		else:
			odd+=1

	return even,odd

even,odd=count(lst)
print("even:{} odd{}".format(even,odd))
