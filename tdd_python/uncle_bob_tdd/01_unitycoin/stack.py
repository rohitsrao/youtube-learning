class UnderflowError(Exception):
    pass

class Stack():

    def __init__(self):
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, element):
        self.size += 1

    def pop(self):
        if self.is_empty() == True:
            raise UnderflowError('Stack is Empty')
        else: 
            self.size -= 1
            return -1
