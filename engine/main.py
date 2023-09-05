from colorama import Fore as col
from colorama import Style
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

    def procinput(self, input):
        """process input

        Args:
            input (str): user's input

        Returns:
            dict: command arguments
        """
        output = {}
        comtoks = input.split(' ')
        for i in enumerate(self.commands):
            if i[1].command == comtoks[0]:
                comtoks.pop(0)
                for j in enumerate(comtoks):
                    output[i[1].comargs[j[0]]] = comtoks[j[0]]
                return i[1].command, output
        print(col.RED + "unknown command: " + comtoks[0])
        print(Style.RESET_ALL, end='\n')
        return ''

class TextManager():
    """Manager for text printing."""
    def __init__(self):
        pass

    def print(self, text):
        """print the given text

        Args:
            text (str): text to print
        """
        print(text)

    def printslow(self, text, delay = 0.2):
        """prints characters of text one at a time

        Args:
            text (str): text to print
            delay (float, optional): delay per charachter in seconds. Defaults to 0.2.
        """
        text = [*str(text)]

        for i in enumerate(text):
            print(i[1], end='', flush=True)
            time.sleep(delay)
        
        print('')
