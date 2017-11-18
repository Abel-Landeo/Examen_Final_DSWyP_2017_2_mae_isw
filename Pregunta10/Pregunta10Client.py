from DocWord import DocWord
from DocContentMemento import DocContentMemento
from CareTaker import CareTaker
class Pregunta10Client(object):
	
	@staticmethod
	def main():
		indexPila = 0
		print("Abriendo doc word..")
		docWord = DocWord()
		print("Preparando CareTaker")
		careTaker = CareTaker()
		docWord.setContent("Muy buenas tardes con todos")
		print("Content: " + docWord.getContent())
		print("Salvando word..")
		careTaker.add(DocContentMemento(docWord.getContent()))
		indexPila += 1

		docWord.setContent("Perdon, muy buenas noches con todos")
		careTaker.add(DocContentMemento(docWord.getContent()))
		print("Actual content: " + docWord.getContent())
		print("Pero estaba bien buenas tardes, reestablecemos")
		docWord.getContentFromMemento(careTaker.get(indexPila))
		indexPila -= 1
