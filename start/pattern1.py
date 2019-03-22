'''
# # # # 
# # # #
# # # #
# # # #
'''

x= int(input("Enter value of N for patterns "))
print("------------------1--------------------")
for i in range(x):
	for j in range(x):
		print("# ",end="")

	print()

print("------------------2--------------------")

for i in range(x):
	for j in range(i+1):
		print("# ",end="")

	print()

print("------------------3--------------------")

for i in range(x):
	for j in range(i,x):
		print("# ",end="")

	print()


