# tuple ( is immutable)
print("--------------tuple-------------\n")
tup=(2,3+5j,'lokesh',5.5,6)
print("tup",tup)
print("tup[2]",tup[2])


print("\n\n--------------set-------------")
s={2,3+5j,'lokesh',5.5,6,2,6}
print("s",s)

print("\n\n--------------dectionary-------------")
d={'int':2,'complex':3+5j,'string':'lokesh','float':5.5,'bool':True}
print("d",d)
print("d['complex']",d['complex'])
print("d.keys()",d.keys())
print("d.values()",d.values())
print("d.get('int')",d.get('int'))

print("\n\n--------------range-------------")
r1=range(10)
r2=range(2,10,2)
print("r1",r1)
print("r2",r2)

print("list(r1)",list(r1))