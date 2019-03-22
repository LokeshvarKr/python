name,age=input("Enter name age comma seperated : ").split(",");
age=int(age)
if name:
	pass
else:
	print("you didn\'t type anything in name")

# if statement
print("-------------------------if---------")
if (age >=18) :
	print( name + " you are adult")


# if-else statement
print("-------------------------if-else--------")
if (age >=18) :
	print( name + " you are adult")
else :
	print(name + " you are not adult")



# nested if
print("-------------------------nested if---------")
if(age >=16):
	print(name+" your are geater than 15 ")
	if(age >= 18):
		print(name+" you are adult ")
	else:
		print(name+" you are not adult ")
else:
	print(name+" you are child now ")

# if-elif-else ladder
print("-----------if-elif-else ladder--------------")
if(age <= 10 ):
	print(name+" you are child under 10 ")
elif(age >=10 and age<= 15):
	print(name+" you are between 11-15 ")
elif(age >=16 and age<= 20):
	print(name+" you are between 16-15 ")
elif(age >=21 and age<= 45):
	print(name+" you are between 21-45 ")
elif(age >=46 and age<= 60):
	print(name+" you are between 46-60 ")
else:
	print(name+" you are old ")

print("-----------in keyword--------------")
if 'h' in name:
	print("yes! 'h' is present in "+name);
else:
	print("no, 'h' is not present in "+name);

print("byeeeeeeeeeeeeeeeeee!")


