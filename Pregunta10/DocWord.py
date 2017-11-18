from DocContentMemento import DocContentMemento

class DocWord:
	
	def __init__(self):
		self.__content = ""

	def setContent(self, content):
		self.__content = content

	def getContent(self):
		return self.__content

	def saveContentToMemento(self):
		return DocContentMemento(self.__content)