#!/usr/bin/python3

# Exercise 2583 from Leetcode, the exercise of the day 10/22/24
# By @urregozw

import unittest

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def sumNodes(self, root, h: dict, depth: int) -> dict:
        if root == None:
            return h

        if depth in h:
            h[depth] += root.val
        else:
            h[depth] = root.val

        self.sumNodes(root = root.left, h = h, depth = depth + 1)
        self.sumNodes(root = root.right, h = h, depth = depth + 1)

        return h


    def kthLargestLevelSum(self, root, k: int) -> int:
        hash_sums = self.sumNodes(root = root, h = {}, depth = 0)
        
        values = list(hash_sums.values())
        values.sort()
        result = len(values) - k
        if result >= 0:
            return values[result]
        else:
            return -1


class TestCases(unittest.TestCase):
    ans = Solution()

    def test_case_1(self):
        root = TreeNode(411310,TreeNode(211244), TreeNode(111674))
        query = self.ans.kthLargestLevelSum(root=root, k=2)

        self.assertEquals(query, 322918)


if __name__ == '__main__':
    unittest.main()