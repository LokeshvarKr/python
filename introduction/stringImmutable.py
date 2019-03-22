# in python strings are immputable 

name="lokesh"
# name[0]='L' (Error! we can't do this)

name.replace('l','L')
print(name)

new_name=name.replace('l','L')
print(new_name)

# but we can do this 
name=name.replace('l','L')
print(name)


# we can use += with string also
name+='**********kumar';
print(name)