class UnderflowError(Exception):
    pass

class Stack():

    def __init__(self):
        self.is_empty = True

    def is_empty(self):
        return self.is_empty

    def push(self, element):
        self.is_empty = False

    def pop(self):
        if self.is_empty == True:
            raise UnderflowError('Stack is Empty')
