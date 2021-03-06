import unittest

def factorsOf(num):
    remainder = num
    factors = []
    divisor = 2
    while remainder > 1:
        while (remainder % divisor == 0):
            factors.append(divisor)
            remainder /= divisor
        divisor += 1
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
        self.assertListEqual(factorsOf(9), [3, 3])
        self.assertListEqual(factorsOf(10), [2, 5])
        self.assertListEqual(factorsOf(2*3*5*7*11*13), [2, 3, 5, 7, 11, 13])
        self.assertListEqual(factorsOf(2*2*3*3*3*5*5*5*5*5), [2, 2, 3, 3, 3, 5, 5, 5, 5, 5])

if __name__ == '__main__':
    unittest.main()
