import unittest

def factorsOf(num):
    remainder = num
    factors = []
    if remainder > 1:
        if (remainder % 2 == 0):
            factors.append(2)
            remainder /= 2
    if (remainder > 1):
        factors.append(remainder)
    return factors

class PrimeFactorsTest(unittest.TestCase):

    def test_factors(self):
        self.assertEqual(len(factorsOf(1)), 0)
        self.assertListEqual(factorsOf(2), [2])
        self.assertListEqual(factorsOf(3), [3])
        self.assertListEqual(factorsOf(4), [2, 2])
        self.assertListEqual(factorsOf(5), [5])
        self.assertListEqual(factorsOf(6), [2, 3])
        self.assertListEqual(factorsOf(7), [7])
        self.assertListEqual(factorsOf(8), [2, 2, 2])

if __name__ == '__main__':
    unittest.main()
