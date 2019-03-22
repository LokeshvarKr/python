'''
class computer:
	def __init__(self):
		print("------init-----")

	def config(self):
		print("config is i5 16gb 1tb")


com1=computer()
com2=computer()

computer.config(com1) # or com1.config()
computer.config(com2) # or com2.config()

'''

class computer:
	#class variables or (static variables of this class)
	brand='dell'
	made_in='japan'

	# def__int__ is constructor in python
	def __init__(self,cpu,ram,hdd):
		#instance variables
		self.cpu=cpu
		self.ram=ram
		self.hdd=hdd
		self.ram_type="DDR4"

	#methods
	def config(self):
		print(self.cpu,self.ram,self.hdd,self.brand,self.made_in)


	def compare_cpu(self,c):
		return self.cpu==c.cpu

	
	# class method work with class variables
	@classmethod
	
	def details(cls):
		print(cls.brand,cls.made_in)
	

	# static method doesnot use class and instance variables
	@staticmethod
	
	def message():
		print("This computer is built and designed for spacial porpose")



com1=computer('i5',16,'1tb')
com2=computer('i7',16,'2tb')
com3=computer('Rezen 3',16,'2tb')

print("------------------------------")
com1.config()
com2.config()
com3.config()

print("------------------------------")
com1.brand='lenovo'
com1.made_in='finland'
com1.config()
com2.config()
com3.config()

print("------------------------------")
computer.brand='hp'
computer.made_in='india'
com1.config()
com2.config()
com3.config()

print("------------------------------")
computer.details()
computer.message()

print("------------------------------")
print("type of com1 ",type(com1))
print("id of com1 ",id(com1))

if com1.compare_cpu(com2):
	print("both has same cpu")
else:
	print("both has different cpu")

print("------------------------------")