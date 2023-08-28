import time
import apil.terminal as terminal

Terminal = terminal.TextInterface()

Terminal.curinput = input('hello')

def wait(timee):
    """
        wait for timee milliseconds
    
        Args: 
        timee (int): milliseconds to wait 
    """

    timee = timee * 1000
    time.sleep(timee)


