from FactoryProducer import FactoryProducer

class Client:
	
	@staticmethod
	def main():
		finishFactory = FactoryProducer.getFactory("finish")
		storageFactory = FactoryProducer.getFactory("storage")
		processorFactory = FactoryProducer.getFactory("processor")
		memoryFactory = FactoryProducer.getFactory("memory")
		basicComputer = Computer(finishFactory.getFinish("white"), storageFactory.getStorage("small"), processorFactory.getProcessor("basic"), memoryFactory.getMemory("basic"))
        print("Basic Computer:\n" + basicComputer.getDescription())
        officeComputer = Computer(finishFactory.getFinish("white"), storageFactory.getStorage("medium"), processorFactory.getProcessor("fast"), memoryFactory.getMemory("advanced"))
        print("Office Computer:\n" + officeComputer.getDescription())
        developerComputer = Computer(finishFactory.getFinish("black"), storageFactory.getStorage("medium"), processorFactory.getProcessor("fast"), memoryFactory.getMemory("pro"))
        print("Developer Computer:\n" + developerComputer.getDescription())
        highEndComputer = Computer(finishFactory.getFinish("black"), storageFactory.getStorage("huge"), processorFactory.getProcessor("high"), memoryFactory.getMemory("pro"))
        print("HighEnd Computer Computer:\n" + highEndComputer.getDescription())
		