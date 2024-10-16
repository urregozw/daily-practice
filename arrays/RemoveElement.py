#!/usr/bin/python3

# Exercise 27 from Leetcode, in the section of arrays
# By @urregozw

import unittest

class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        '''
            Time: O(N)
            Space: O(1)
        '''
        i = 0
        count = 0
        l = len(nums)
        while i < l - count:
            num = nums[i]
            if num == val:
                nums[i] = nums[l - 1 - count]
                count += 1
            else:
                i += 1
        
        
        return l - count

class TestCase(unittest.TestCase):
    ans = Solution()
    def test_case_1(self):
        query = self.ans.removeElement([0,1,2,2,3,0,4,2], 2)
        self.assertEqual(query, 5)
        

if __name__ == "__main__":
    unittest.main()
