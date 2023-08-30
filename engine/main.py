import time

def wait(timee):
    """
        wait for timee milliseconds
    
        Args: 
        timee (int): milliseconds to wait 
    """

    timee = timee * 1000
    time.sleep(timee)

class Command():
    """command"""
    def __init__(self, command, comargs):
        self.command = command
        self.comargs = []

        for i in enumerate(comargs):
            self.comargs.append(i[1])

class Commanager():
    """
    manages command interface
    """
    def __init__(self):
        self.commands = []

    def addcom(self, command, comargs):
        self.commands.append(Command(command, comargs))

    def procinput(self, input = str()):
        output = {}
        comtoks = input.split(' ')
        for i in enumerate(self.commands):
            if i[1].command == comtoks[0]:
                comtoks.pop(0)
                for j in enumerate(comtoks):
                    output[i[1].comargs[j[0]]] = comtoks[j[0]]
