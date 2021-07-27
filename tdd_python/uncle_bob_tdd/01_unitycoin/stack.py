class UnderflowError(Exception):
    pass

class Stack():

    def __init__(self):
        self.size = 0
        self.elements = []

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def push(self, element):
        self.size += 1
        self.elements.append(element)

    def pop(self):
        if self.is_empty() == True:
            raise UnderflowError('Stack is Empty')
        else: 
            self.size -= 1
            popped_element = self.elements[-1]
            del self.elements[-1]
            return popped_element
