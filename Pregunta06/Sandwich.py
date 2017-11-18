from abc import ABCMeta, abstractmethod

class Sandwich(metaclass=ABCMeta):
	
	@abstractmethod
	def make(self): pass