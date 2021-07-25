import unittest

from library import Library
from movie import Movie

class DonateMovieTest(unittest.TestCase):

    def setUp(self):
        self.movie = Movie()
        self.library = Library()
        self.library.donate(self.movie)


    def test_donate_movie(self):
        self.assertTrue(self.library.contains(self.movie))
        self.assertEqual(1, self.movie.get_copies())

if __name__ == '__main__':
    pass
