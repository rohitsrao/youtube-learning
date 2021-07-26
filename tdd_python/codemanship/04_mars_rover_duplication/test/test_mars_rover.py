import unittest

from rover import Rover

class MarsRoverTest(unittest.TestCase):

    def test_turn_right_N_to_E(self):
        rover = Rover('E')
        self.assertEqual('E', rover.facing)

if __name__ == '__main__':
    unittest.main()
