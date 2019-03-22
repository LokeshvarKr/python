from math import pow
class math:
	def __init__(self):
		self.seed=1
		self.m=pow(2,31)
		self.a=166525
		self.c=101394223
	
	def next_int_random(self,Range):
		self.seed=(self.a*self.seed+self.c)%self.m
		return self.seed%Range
	

print("=============FOR SMALL SEED===================")
m=math()
s=set()
for i in range(5000000):
	y=m.next_int_random(110000)
	if y in s:
		print("REPEAT AT ",i)
		break
	s.add(y)
print("==============================================")
