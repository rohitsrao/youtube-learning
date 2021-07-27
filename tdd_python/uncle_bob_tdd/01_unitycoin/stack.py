class UnderflowError(Exception):
    pass

class Stack():

    def __init__(self):
        self.elements = []

    def is_empty(self):
        if len(self.elements) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        if self.is_empty() == True:
            raise UnderflowError('Stack is Empty')
        else: 
            popped_element = self.elements[-1]
            del self.elements[-1]
            return popped_element
