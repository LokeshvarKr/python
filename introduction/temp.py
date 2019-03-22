name,char = input("Enter name and character by comma seperated\n").split(",");
print(name);
print(len(name));
print(name.count(char));
print(name.lower().count(char.lower()));
print("byeeeeeeeeeeeeeeee!");

# using replace
print(name.replace(" ","").lower().count(char.replace(" ","").lower()))
# or this was also in multiple line (but more clear )
name=name.replace(" ","")
char=char.replace(" ","")
print(name.lower().count(char.lower()))
