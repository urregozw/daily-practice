#!/usr/bin/python3

# Exercise 941 from Leetcode, the exercise of the day 10/17/24
# By @urregozw

import unittest

class Solution:
    def validMountainArray(self, arr: list) -> bool:
        if len(arr) < 3:
            return False
        
        summit = max(arr)
        pivot = arr.index(summit)
        ascending, descending = False, False
        for i in range(len(arr[:pivot + 1])):
            if i + 1 > pivot: break
            descending = True
            base = arr[i]
            step = arr[i + 1]
            if base >= step:
                return False
            
        
        for j in range(pivot, len(arr)):
            if j + 1 >= len(arr): break
            ascending = True
            base = arr[j]
            step = arr[j + 1]
            if base <= step:
                return False

            
        
        return True and ascending and descending


class TestCase(unittest.TestCase):
    ans = Solution()

    def test_case_1(self):
        query = self.ans.validMountainArray([0,1,2,3,4,5,6,7,8,9])
        self.assertEqual(query, False)

if __name__ == '__main__':
    unittest.main()    