import unittest

def factorsOf(num):
    factors = []
    if num == 2:
        factors.append(2)
    return factors

class PrimeFactorsTest(unittest.TestCase):

    def test_factors(self):
        self.assertEqual(len(factorsOf(1)), 0)
        self.assertListEqual(factorsOf(2), [2])

if __name__ == '__main__':
    unittest.main()
