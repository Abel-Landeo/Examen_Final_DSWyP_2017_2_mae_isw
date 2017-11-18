from SandwichDecorator import SandwichDecorator

class EggSandwichDecorator(SandwichDecorator):
	
	def make(self, sandwich):
		self.__addEgg(sandwich)
		sandwich.make()

	def __addEgg(self, sandwich):
		print("Adding Egg to sandwich")
		
