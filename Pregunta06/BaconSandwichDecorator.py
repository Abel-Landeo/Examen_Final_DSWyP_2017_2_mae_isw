from SandwichDecorator import SandwichDecorator

class BaconSandwichDecorator(SandwichDecorator):
	
	def make(self, sandwich):
		self.__addBacon(sandwich)
		sandwich.make()

	def __addBacon(self, sandwich):
		print("Adding Bacon to sandwich")