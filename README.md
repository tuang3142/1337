# the purpose is to showcase tdd & clean code

tdd on ds and algorithms
implement them from sratch 1 hour a day
the rest dont matter

# Why

This repo contains my solutions for [leetcode](http://leetcode.com/) problems. Occasionally, I'll write algorithms and data structures from scratch. The purpose is to practice and showcase clean and test-driven code. I primarily use python over ruby (which I use professionally) because python supports a wider range of libraries for solving algorithmic problems.  
Each solution comes with an explanation and test suites. I'll keep them brief as it takes great effort to write an "easy-to-understand" explanation and an equal effort to understand it. Again, the punch line is only "clean and test-driven" code.

# How to test

Using Vim (which you should) with the `vim-test` plugin, open a test file and run `:TestFile`. At the moment, I'm only writing python test.

# Examples

## 239. Sliding Window Maximum


### tl;dr

[Link to the original problem.](https://leetcode.com/problems/sliding-window-maximum/)  
Given an array of integers `A` and a window of size `k`, return the largest number in the window when moving it from left to right one index at a time.
```
Input: A = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

Window position                Max
----------------------------------
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

### Idea

This problem is more commonly known as [monotonic queue](http://www.algorithmsandme.com/monotonic-queue/). The idea is to create a queue and make sure the order is decreasing so that the first number in q is always the largest.

### Complexity

With `n = len(A)`:
- time: `O(n)`
- space: `O(n)`


### Code

`solution.py`

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, A, k):
        qu = deque()
        ret = []
        for i in range(len(A)):
            while qu and A[i] >= A[qu[-1]]: # keep the qu in decreasing order
                qu.pop()                    # make sure the first number in qu is the largest
            qu.append(i)
            if i < k - 1:                   # appending the first k numbers to qu
                continue
            while qu and i - qu[0] + 1 > k: # pop the first in qu if it is out of window range
                qu.popleft()
            ret.append(A[qu[0]])
        return ret
```

`test.py`

```python
import unittest
from solution import Solution

class Test(unittest.TestCase):
    def test_general_cases(self):
        A = [1,3,-1,-3,5,3,6,7]
        k = 3
        self.assertEqual(Solution().maxSlidingWindow(A, k), [3,3,5,5,6,7])

        A = [7,2,4]
        k = 2
        self.assertEqual(Solution().maxSlidingWindow(A, k), [7, 4])

    def test_k_equal_1(self):
        A = [-1, 2, 3]
        k = 1
        self.assertEqual(Solution().maxSlidingWindow(A, k), [-1, 2, 3])

    def test_k_equal_array_length(self):
        A = [-1, 2, 3]
        k = 3
        self.assertEqual(Solution().maxSlidingWindow(A, k), [3])

if __name__ == '__main__':
    unittest.main()
```

## 1367. Linked List in Binary Tree


### tl;dr

[Link to the problem statement.](https://leetcode.com/problems/linked-list-in-binary-tree/)  
Given the root of a binary tree `root` and the head of a linked list `head`, check if all the nodes in the linked list starting from the head correspond to some downward path connected in the tree.
```
Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: blue nodes form a path in the tree that is "equal" to the linked list.
```
![visualized tree](https://assets.leetcode.com/uploads/2020/02/12/sample_1_1720.png "image from leetcode.com")
### Idea

This problem is similar to finding a pattern in a string. The brute force approach is acceptable. However, we can use [KMP algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm) to produce a much faster solution. The idea is when checking if a tree node is in the linked list, we don't need to start all over from beginning of the list.


### Complexity

with `n = number_of_tree_nodes` and `k = number_of_list_nodes`:
- time: `O(n + k)`
- space: `O(k)` (because we need to transform the list into a k-sized array, which makes me wonder why they gave the list at the first place but well, hate the game dont hate the player)

### Code

The python implementation for `Tree` and `LinkedList` can be found under `data_structure/`.  

`solution.py`

```python
class Solution:
    def isSubPath(self, head, root):
        A, lps = self.convert_to_array(head) # lps = longest "prefix which is also suffix"
        def visit(node, i):
            if i >= len(A):
                return True
            if not node:
                return False
            if node.val == A[i]:
                return(visit(node.left, i + 1) or visit(node.right, i + 1))
            if i > 0:
                return visit(node, lps[i - 1])
            return visit(node.left, 0) or visit(node.right, 0)

        return visit(root, 0)

    def convert_to_array(self, node):
        A = []
        while node:
            A.append(node.val)
            node = node.next
        lps = [0] * len(A)
        i, j = 1, 0
        while i < len(A):
            if A[i] == A[j]:
                lps[i] = j + 1
                i, j = i + 1, j + 1
            else:
                if j > 0: j = lps[j - 1]
                else: i += 1
        return A, lps
```

`test.py`

```python
import sys, os
sys.path.append(os.path.abspath("./data_structure"))
import unittest
from linked_list import LinkedList
from tree import Tree
from solution import Solution

class Test(unittest.TestCase):
    def setUp(self):
        self.isSubPath = Solution().isSubPath

    def test_general(self):
        head = LinkedList.convert_array([4,2,8])
        root = Tree.convert_array([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
        self.assertEqual(self.isSubPath(head, root), True)

        head = LinkedList.convert_array([1,4,2,6])
        root = Tree.convert_array([1,4,4,None,2,2,None,1,None,6,8,None,None,None,None,1,3])
        self.assertEqual(self.isSubPath(head, root), True)

    def test_len_head_is_1(self):
        head = LinkedList(7)
        root = Tree.convert_array([1, 7])
        self.assertEqual(self.isSubPath(head, root), True)

    def test_head_is_longer_than_tree_depth(self):
        head = LinkedList([1, 2, 3, 4, 5])
        root = Tree.convert_array([1, 2])
        self.assertEqual(self.isSubPath(head, root), False)

if __name__ == '__main__':
    unittest.main()
```
