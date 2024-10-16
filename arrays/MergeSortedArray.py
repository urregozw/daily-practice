#!/usr/bin/python3

# Exercise 88 from Leetcode, in the section of arrays
# By @urregozw

import unittest

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Time: O(N+M Log(N+M))
        Space: O(1)
        """
        for num in nums2:
            nums1[m] = num
            m += 1

        nums1.sort() 

        return nums1 # It only returns for the tests


class TestCases(unittest.TestCase):
    ans = Solution()

    def test_case_1(self):
        query = self.ans.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
        self.assertEqual(query, [1,2,2,3,5,6])


if __name__ == "__main__":
    unittest.main()
