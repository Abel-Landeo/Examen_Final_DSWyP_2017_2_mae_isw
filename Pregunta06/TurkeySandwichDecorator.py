from SandwichDecorator import SandwichDecorator

class TurkeySandwichDecorator(SandwichDecorator):
	
	def make(self, sandwich):
		self.__addTurkey(sandwich)
		sandwich.make()

	def __addTurkey(self, sandwich):
		print("Adding Turkey to sandwich")