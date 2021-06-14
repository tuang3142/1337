import unittest
from solution import Solution


class Test(unittest.TestCase):
    def setUp(self):
        self.maximumRemovals = Solution().maximumRemovals

    # example cases, can be solved by hand, given in statement
    def test_general(self):
        s = "abcacb"; p = "ab"; removable = [3,1,0]
        self.assertEqual(self.maximumRemovals(s, p, removable), 2)

        s = "abcbddddd"; p = "abcd"; removable = [3,2,1,4,5,6]
        self.assertEqual(self.maximumRemovals(s, p, removable), 1)

        s = "abcab"; p = "abc"; removable = [0,1,2,3,4]
        self.assertEqual(self.maximumRemovals(s, p, removable), 0)

    # really small/large cases, usually 0 or n
    # def test_edge(self):

    # def test_no_solution(self):

    # not edge case, but could fail if not handle properly
    # def test_tricky(self):


if __name__ == '__main__':
    unittest.main()
