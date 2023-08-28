

class TextInterface():
    """
    Text interface for engine API.
    """
    def __init__(self):
        self.curinput = None

    def print(self, text):
        """prints the given text

        Args:
            text (str): the text to print
        """

        print(text)

    def reqestinput(self):
        """
            passes the input from engine to the user
        """

        return self.curinput

class CmdManager(TextInterface):
    """
    Manages command IO
    """
    def __init__(self):
        TextInterface.__init__(self)

    def reqcommand(self, command, args, input):
        pass
