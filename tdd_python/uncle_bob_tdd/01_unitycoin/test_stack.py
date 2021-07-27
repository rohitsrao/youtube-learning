import unittest

from stack import Stack, UnderflowError

class StackTest(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()

    def test_new_stack_is_empty(self):
        self.assertTrue(self.stack.is_empty())

    def test_after_one_push_is_not_empty(self):
        self.stack.push(0)
        self.assertFalse(self.stack.is_empty())

    def test_exception_when_empty_stack_popped(self):
        self.assertRaises(UnderflowError, self.stack.pop)

    def test_after_one_push_one_pop_will_be_empty(self):
        self.stack.push(0)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_after_two_pushes_one_pop_will_not_be_emtpy(self):
        self.stack.push(0)
        self.stack.push(1)
        self.stack.pop()
        self.assertFalse(self.stack.is_empty())

    def test_after_pushing_X_will_pop_X(self):
        self.stack.push(99)
        self.stack.pop()
        self.stack.push(88)
        self.assertEqual(88, self.stack.pop())

