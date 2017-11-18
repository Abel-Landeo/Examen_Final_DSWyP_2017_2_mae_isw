from SandwichDecorator import SandwichDecorator

class BeefSandwichDecorator(SandwichDecorator):
	
	def make(self, sandwich):
		self.__addBeef(sandwich)
		sandwich.make()

	def __addBeff(self, sandwich):
		print("Adding Beef to sandwich")