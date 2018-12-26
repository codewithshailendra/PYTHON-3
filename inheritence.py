class A:
	def feature1(self):
		print("Feature 1 working")

	def feature2(self):
		print("feature 2 is working")

# single level inheritence
class B(A): # class B is subclass of class A or class B inherit class A.

	def feature3(self):
		print("Feature 3 working")

	def feature4(self):
		print("feature 4 is working")



class C(B):  # multilevel inheritence

	def feature5(self):
		print("feature 5 is working")



class D(A,b):  # multiple inheritance
	def feature6(self):
		print("Feature 6 working")

	def feature7(self):
		print("feature 7 is working")




a1=A()
a1.feature1()	
a1.feature2()

b1=B()
b1.feature3()
b1.feature4()

c1=C()
c1.feature1()


# multiple level of inheritance:when a single class inherites two completely different classes
