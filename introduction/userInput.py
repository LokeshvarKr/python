# input() always takes input as a string 
name=input("Enter ur name\n")
age=input("Enter ur age\n")
print("-------------Entered value--------------------")
print("Hello  "+name)
print("age "+age)

a=input("Enter value of a (number)\n")
b=input("Enter value of b (number)\n")
print('#wrong addition of two numbers (it is string addition)')
print("total "+a+b)

a=int(a)
b=int(b)
print('#correct in float addition of two numbers')
print("total "+ str(a+b))

print("---------------------------------")

# input convert in integer
# a=int(input("Enter value of a (number)\n"))
# b=int(input("Enter value of b (number)\n"))
# print("total "+ str(a+b))

# floating addition
a=float(a)
b=float(b)

print('#correct addition of two numbers')
print("total "+ str(a+b))
print("---------------------------------")
name,age="Harsha",23
x=y=z=2+3;
print("Name "+name+" "+"age"+" "+str(age))
print(str(x)+" "+str(y)+" "+str(z))