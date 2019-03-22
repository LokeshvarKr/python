from math import pow
class math:
	def __init__(self):
		self.x=1
		self.m=pow(2,31)
		self.a=1664525
		self.c=1013904223
		self.output=int('0b00111111111111110000000000000000',2)
		self.long_output=int('0b00111111111111111111111111111111',2)


	def next_int_random(self):
		self.x=(self.a*self.x+self.c)%self.m
		return (int(self.x)&self.output)
	
	def next_long_int_random(self):
		self.x=(self.a*self.x+self.c)%self.m
		return (int(self.x)&self.long_output)
	

print("=============FOR SMALL SEED===================")
m=math()
s=set()
for i in range(5000000):
	y=m.next_int_random()
	if y in s:
		print("REPEAT AT ",i)
		break
	s.add(y)
s.clear()
print("=============FOR BIG SEED===================")
for i in range(5000000):
	y=m.next_long_int_random()
	if y in s:
		print("REPEAT AT ",i)
		break
	s.add(y)
print("==============================================")

print("=============FOR SMALL SEED===================")
m=math()
s=set()
for i in range(5000000):
	y=m.next_int_random()
	if y in s:
		continue
	s.add(y)
print(len(s))
s.clear()
print("=============FOR BIG SEED===================")
s.clear()
for i in range(5000000):
	y=m.next_long_int_random()
	if y in s:
		continue
	s.add(y)
print(len(s))
print("==============================================")
