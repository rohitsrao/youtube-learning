class Movie:

    def __init__(self):
        self._copies = 0

    def add_copy(self):
        self._copies += 1

    def get_copies(self):
        return self._copies
