import os

class View(object):
    """ Cette classe sert à communiquer des informations 
    à l'opérateur du serveur. """

    def __init__(self, parent):
        self.parent = parent

    def print_console(self,message):
        print(message)

        