import unittest

from stack import Stack

class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty)

    def test_push(self):
        self.stack.push(0)
        self.assertTrue(not self.stack.is_empty)

