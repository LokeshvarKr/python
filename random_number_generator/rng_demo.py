from math import pow
class math:
	def __init__(self):
		self.seed=1
		self.m=pow(2,31)
		self.a=1665525
		self.c=1013904223
	
	def next_int_random(self):
		self.seed=(self.a*self.seed+self.c)%self.m
		return self.seed
	

print("=============FOR SMALL SEED===================")
m=math()
s=set()
for i in range(5000000):
	y=m.next_int_random()
	if y in s:
		print("REPEAT AT ",i)
		break
	s.add(y)
print("Total diff Numbers: ",len(s))
print("==============================================")
