import random
for x in range(10):
	print("random number from list is :",end="")
	print (random.choice([1,12,3,11,6,78,43,15,56,71,4]))

print("-----------------------------")
for x in range(10):
	print("random number from range is :",end="")
	print (random.randrange(1,101));

print("-----------------------------")
for x in range(10):
	print("random number from range is :",end="")
	print (random.randrange(100000000,2000000000));

print("-----------------------------")
for x in range(10):
	print("random number from range is :",end="")
	print (random.randrange(1000000,2000000000,3456765));

