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
        self.assertEqual(1, movie.copies)

if __name__ == '__main__':
    pass
