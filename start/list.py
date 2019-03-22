#list
print("-----------------1-------------")
name=['harsha','komal','rani','kiran']
age=[20,21,22,22.4]
mix=[name,age]
mixture=['lokesh',23,'m170364ca','mca',2412]


print("name",name)
print("age",age)
print("mix",mix)
print("mixture",mixture)

print("-----------------2-------------")
a=[2,2,1,4,11,21,3,2,12]

print(a)

a.append(23)
print("a.append(23)",a)

a.insert(2,323)
print("a.insert(2,323)",a)

a.pop()
print("a.pop()",a)

a.pop(3)
print("a.pop(3)",a)

a.sort()
print("a.sort()",a)

print("a.count(2)",a.count(2))
print("len(a)",len(a))
print("min",min(a))
print("max",max(a))
print("sum",sum(a))