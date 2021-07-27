import unittest

from stack import Stack

class StackTest(unittest.TestCase):

    def test_new_stack_is_empty(self):
        stack = Stack()
        self.assertTrue(stack.is_empty)

    def test_push(self):
        stack = Stack()
        stack.push(0)
        self.assertTrue(not stack.is_empty)

