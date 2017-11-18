from SandwichDecorator import SandwichDecorator

class ChickenSandwichDecorator(SandwichDecorator):
	
	def make(self, sandwich):
		self.__addChiken(sandwich)
		sandwich.make()

	def __addChiken(self, sandwich):
		print("Adding Chiken to sandwich")