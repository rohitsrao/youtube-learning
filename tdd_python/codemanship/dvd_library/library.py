from movie import Movie

class Library:

    def __init__(self):
        self._catalouge = []
    
    def donate(self, movie):
        self._catalouge.append(movie)
        movie.add_copy()

    def contains(self, movie):
        return (movie in self._catalouge)

