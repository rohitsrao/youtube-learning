import unittest

from stack import Stack

class StackTest(unittest.TestCase):

    def test_create_stack(self):
        stack = Stack()
        self.assertTrue(stack.is_empty())

