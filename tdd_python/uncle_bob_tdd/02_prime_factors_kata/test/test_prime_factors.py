import unittest

def factorsOf(num):
    return []

class PrimeFactorsTest(unittest.TestCase):

    def test_factors(self):
        self.assertEqual(len(factorsOf(1)), 0)

if __name__ == '__main__':
    unittest.main()
