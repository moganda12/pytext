import time

def wait(timee):
    """
        wait for timee milliseconds
    
        Args: 
        timee (int): milliseconds to wait 
    """

    timee = timee * 1000
    time.sleep(timee)


