#!/usr/bin/python3

# Exercise 26 from Leetcode, in the section of arrays
# By @urregozw

import unittest

class Solution:
    def removeDuplicates(self, nums: list) -> int:
        '''
            T.C: O(N) 
            S.C: O(1)
        '''
        unique = 1
        duplicated = nums[0]
        for i in range(1, len(nums)):
            val = nums[i]
            if val != duplicated:
                duplicated = val
                nums[unique] = val
                unique += 1
        
        return unique


class TestCase(unittest.TestCase):
    ans = Solution()
    def test_case_1(self):
        query = self.ans.removeDuplicates(nums = [1,1,2])
        self.assertEqual(query, 2)
        

if __name__ == "__main__":
    unittest.main()