class Stack():

    def __init__(self):
        self.is_empty = True

    def is_empty(self):
        return self.is_empty

    def push(self, element):
        self.is_empty = False
