class students:

	college="IIT(BHU)VARANASI"  # class variable


	def __init__(self,m1,m2,m3):
		self.m1=m1
		self.m2=m2
		self.m3=m3

	def avg(self):
		return (self.m1+self.m2+self.m3)/3

	def getM1(self):   # accessor method
		return self.m1

	def setM1(self):    # mutator method
		return self.m2

	@staticmethod
	def info():  # static method, it has nothing to do class or instance variable.
	print("This is the class of students")


	@classmethod   # decorators

	def get_college(cls):   # class method
		return cls.college
    




s1 = students(12,23,43)
s2 = students(45,65,34)

print(s1.avg())

print(students.get_college()) # works even without writing decorator
print(students.get_college()) # works after writing decoratoe