
class CareTaker:
	
	def __init__(self):
		self.__mementoList = []

	def add(self, docContentMemento):
		self.__mementoList.append(docContentMemento)

	def get(self, index):
		return self.__mementoList[index]