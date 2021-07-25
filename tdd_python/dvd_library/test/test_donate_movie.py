import unittest

from library import Library
from movie import Movie

class DonateMovieTest(unittest.TestCase):

    def setUp(self):
        self.movie = Movie()
        self.library = Library()
        self.library.donate(self.movie)


    def test_add_movie_to_library(self):
        self.assertTrue(self.library.contains(self.movie))

    def test_copy_added(self):
        self.assertEqual(1, self.movie.get_copies())

if __name__ == '__main__':
    pass
