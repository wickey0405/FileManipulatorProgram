import abc
from command import Command
import os

class CommandReplace(Command):
    def __init__(self,name):
        self.name = name

    def isAvailable(self, userInput):
        if len(userInput) != 4:
            return False
        
        if userInput[0] != self.name:
            return False

        if type(userInput[1]) != str:
            return False

        if os.path.isfile(userInput[1]):
            return False

    def runCommand(self, userInput):
        if self.isAvailable(userInput): 
            print("your command is not available.")
            return
        
        inputPath = userInput[1]
        target  = userInput[2]
        newWord = userInput[3]
        contents = ""

        with open(inputPath) as f:
            contents = f.read()

        with open(inputPath, 'w') as f:
            f.write(contents.replace(target, newWord))
