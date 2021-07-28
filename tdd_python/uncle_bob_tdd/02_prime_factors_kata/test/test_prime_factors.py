import unittest

def factorsOf(num):
    factors = []
    if num > 1:
        factors.append(num)
    return factors

class PrimeFactorsTest(unittest.TestCase):

    def test_factors(self):
        self.assertEqual(len(factorsOf(1)), 0)
        self.assertListEqual(factorsOf(2), [2])
        self.assertListEqual(factorsOf(3), [3])

if __name__ == '__main__':
    unittest.main()
