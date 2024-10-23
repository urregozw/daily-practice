#!/usr/bin/python3

# Exercise from the day, 10/23/24
# By @urregozw

import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def cousinsBinaryTree(self, root: TreeNode, depth: int, parent:TreeNode, cousins: list) -> list:
        if root == None:
            return cousins

        self.cousinsBinaryTree(root=root.left, depth=depth + 1, parent=root, cousins=cousins)
        self.cousinsBinaryTree(root=root.right, depth=depth + 1, parent=root, cousins=cousins)
        h = cousins[depth]
        if parent in h:
            h[parent] = h[parent] + root.val
        else:
            h[parent] = root.val
        
        cousins[depth] = h
        
        return cousins
            

    def cousinTree(self, root: TreeNode, depth: int, parent: TreeNode, cousins: list) -> TreeNode:
        if root == None:
            return root
        
        if parent == None:
            root.val = 0
        else:
            h = cousins[depth]
            total = 0
            for key, value in h.items():
                if key != parent:
                    total += value
            
            root.val = total
            #left = parent.left.val if parent.left != None else 0
            #right = parent.right.val if parent.right != None else 0
            

        self.cousinTree(root=root.right, depth=depth + 1, parent=root, cousins=cousins)
        self.cousinTree(root=root.left, depth=depth + 1, parent=root, cousins=cousins)
        
        return root


    def replaceValueInTree(self, root: TreeNode) -> TreeNode:
        cousins = [dict() for x in range(pow(10, 5))]
        cousins = self.cousinsBinaryTree(root=root, depth=0, parent=None, cousins=cousins)
        root = self.cousinTree(root=root, depth=0, parent=None, cousins=cousins)
        return root


class TestCases(unittest.TestCase):
    ans = Solution()
    
    def test_case_1(self):
        query = self.ans.replaceValueInTree(TreeNode(val=2, left= TreeNode(val= 3), right = TreeNode(val=4)))
        self.assertEqual(query.val, 0)


if __name__ == '__main__':
    unittest.main()