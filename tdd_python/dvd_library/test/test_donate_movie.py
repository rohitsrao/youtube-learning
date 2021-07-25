import unittest

from library import Library
from movie import Movie

class DonateMovieTest(unittest.TestCase):

    def test_donate_movie(self):
        movie = Movie()
        library = Library()
        library.donate(movie)
        #self.assertTrue(movie in library.catalouge)
        self.assertTrue(library.contains(movie))

if __name__ == '__main__':
    pass
