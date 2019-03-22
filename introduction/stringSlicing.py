name="RamGopalVermaKesari"
print("name "+name)
print(name[0])
#slicing syntax--> array[start argument : stop argument + 1]
#this will print starting from index 2 and end at index 5
print(name[2:6])
#this will print starting from index 1 and end at index 5
print(name[1:6])
#this will print starting from index -1 and end at index 5
print(name[-10:12])
#print whole string
print(name[:])
#print from 2 to all rest
print(name[2:])
#print from starting to till index 5
print(name[:5])
#print from -3 to rest
print(name[-3:])

print("lokeshHarsha"[2:7])
print("----------------------")
# step argument
#slicing syntax--> array[start argument : stop argument + 1 : step argument]
print("lokeshHarsha"[2:7:1])
print("lokeshHarsha"[2:7:2])
print("lokeshHarsha"[2:7:3])

print("lokeshHarsha"[2::2])
print("lokeshHarsha"[2::3])
print("lokeshHarsha"[::1])
print("lokeshHarsha"[::2])

print("lokeshHarsha"[10::-1])
print("lokeshHarsha"[10::-2])
print("lokeshHarsha"[-1::-1])
print("lokeshHarsha"[-1::-2])
# trick for reversing the string 
print("lokeshHarsha"[::-1])

name=input("Enter Name\n")
print("reversed name is "+name[::-1])
print("reversed name is {}".format(name[::-1]))