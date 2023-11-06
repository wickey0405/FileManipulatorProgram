import abc
from command import Command
import os

class CommandCopy(Command):
    def __init__(self,name):
        self.name = name

    def isAvailable(self, userInput):
        if len(userInput) != 3:
            return False
        
        if userInput[0] != self.name:
            return False

        if type(userInput[1]) != str or type(userInput[2]) != str:
            return False

        if os.path.isfile(userInput[1]) or os.path.isfile(userInput[2]):
            return False
        
        if userInput[1] == userInput[2]:
            return False

    def runCommand(self, userInput):
        if self.isAvailable(userInput): 
            print("your command is not available.")
            return
        
        inputPath = userInput[1]
        outputPath  = userInput[2]
        contents = ""

        with open(inputPath) as f:
            contents = f.read()

        with open(outputPath, 'w') as f:
            f.write(contents)
