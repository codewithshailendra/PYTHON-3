class students:

	def __init__(self,name,rollno):
		self.name=name
		self.rollno=rollno
		self.lap=self.Laptop()

	def show(self):
		print(self.name,self.rollno)
		self.lap.show()

	class Laptop:   # inner class of the student

		def __init__(self):
			self.brand='HP'
			self.cpu='i7'
			self.RAM=16

		def show(self):
			print(self.brand,self.cpu,self.RAM)



s1=students("shailendra",1)
s2=students("shailu",2)

lap1=s1.lap
lap2=s2.lap
# another way to make object of inner class is as follows:

l1=students.Laptop()

s1.show()



