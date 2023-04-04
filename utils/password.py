from random import choice
from .constants import all

class Password:
    def __init__(self):
        self = self.__init__
        
    def pwdSize(self):
        size = choice(range(12))
        while size <=8:
            size = choice(range(12))
        return size

    def generate(self):
        self.password = ''.join([choice(all) for a in range(self.pwdSize())])
        return self.password
