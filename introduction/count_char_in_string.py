string=input("Enter a string : ")
m=0
temp_var=""
print("---------using while loop-----------")
while m < len(string) :
	char=string[m];
	if temp_var.find(char) >= 0:
		pass
	else:
		c=string.count(char)
		print(" '{}' is {} times".format(string[m],c))
		temp_var=temp_var+char
	m=m+1;
print(temp_var)

print("---------using for loop-----------")
temp_var=""
for i in range(len(string)):
	if temp_var.find(string[i]) >=0 :
		pass
	else:
		c=string.count(string[i]);
		print(" '{}' : {} ".format(string[i],c))
		temp_var+=string[i];

print(temp_var)

print("---------using for loop-----------")
temp_var=""
for i in range(len(string)):
	if string[i] not in temp_var :
		c=string.count(string[i]);
		print(" '{}' : {} ".format(string[i],c))
		temp_var+=string[i];

print(temp_var)