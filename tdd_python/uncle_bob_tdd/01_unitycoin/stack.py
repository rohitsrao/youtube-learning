class UnderflowError(Exception):
    pass

class Stack():

    def __init__(self):
        self.size = 0
        self.element = None

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, element):
        self.size += 1
        self.element = element

    def pop(self):
        if self.is_empty() == True:
            raise UnderflowError('Stack is Empty')
        else: 
            self.size -= 1
            return self.element
