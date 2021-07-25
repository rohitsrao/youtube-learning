class Movie:

    def __init__(self):
        self.copies = 0

    def add_copy(self):
        self.copies += 1

    def get_copies(self):
        return self.copies
