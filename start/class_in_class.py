class student:
	branch="cse"
	course="b.tech"
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
		self.batch="A"
		# object of inner class inside the outer class 
		self.lap=self.computer()


	def show(self):
		print(self.name,self.roll,self.branch)
		self.lap.show()

	# inner class
	class computer:
		brand='hp'
		def __init__(self):
			self.cpu='i5'
			self.ram='16gb'
			self.hdd='1tb'

		def show(self):
			print(self.cpu,self.ram,self.hdd,self.brand)



#outside object of outer class
s1=student("Lokesh","cs892")
s1.show()

#outside object of inner class
lap1=student.computer()
lap1.show()