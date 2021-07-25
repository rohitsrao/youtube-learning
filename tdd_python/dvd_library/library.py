from movie import Movie

class Library:

    def __init__(self):
        self.catalouge = []
    
    def donate(self, movie):
        self.catalouge.append(movie)
        movie.add_copy()

    def contains(self, movie):
        return (movie in self.catalouge)

