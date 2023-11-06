import abc

class Command(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def isAvailable(self, userInput):
        pass

    @abc.abstractmethod
    def runCommand(self, userInput):
        pass