class Display:
    def __init__(self):
        self.commandList = []

    def parseInput(self, strList):
        command = strList[1]
        idx = self.commandList.index([x for x in self.commandList if x.name == command][0])
        if idx == -1:
            print("your command is not defined.")
            return
        self.commandList[idx].runCommand(strList[1:])
    
    def addCommand(self, newCommand):
        self.commandList.append(newCommand)

