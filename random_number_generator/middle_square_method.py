
class math:
	def __init__(self,seed):
		self.seed=int(seed)
		self.digit=len(str(seed))
		self.division=""
		for i in range(self.digit):
			self.division+="9"
		self.division=int(self.division)

	def next_random(self):
		x=self.seed*self.seed
		x=str(x)
		while len(x) < self.digit:
			x="0"+x
		start=self.digit//2
		end=start+self.digit
		self.seed=int(x[start:end])
		if self.seed is 0:
			self.seed=56789
		return self.seed
	
	def next_random_float(self):
		return self.next_random()/self.division

print("=============FOR SMALL SEED==============")
m=math(12345)
s=set()
for i in range(500000):
	y=m.next_random()
	if y in s:
		print("REPEAT AT ",i)
		break
	s.add(y)

s.clear()

m1=math(12345)
for i in range(500000):
	y=m.next_random_float()
	if y in s:
		print("REPEAT AT ",i)
		break
	s.add(y)
print("==============================================")
print("=============FOR BIG SEED==============")
m=math(123456784)
s=set()
for i in range(500000):
	y=m.next_random()
	if y in s:
		print("REPEAT AT ",i)
		break
	s.add(y)

s.clear()

m1=math(123456784)
for i in range(500000):
	y=m.next_random_float()
	if y in s:
		print("REPEAT AT ",i)
		break
	s.add(y)

print("==============================================")
