import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.foo = Solution().foo

    # example cases, can be solved by hand, given in statement
    def test_general(self):
        self.assertEqual(self.foo(), 0)

    # really small/large cases, usually 0 or n
    # def test_edge(self):

    # def test_no_solution(self):

    # not edge case, but could fail if not handle properly
    # def test_tricky(self):


if __name__ == '__main__':
    unittest.main()
