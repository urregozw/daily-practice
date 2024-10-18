#!/usr/bin/python3

# Exercise 1299 from Leetcode
# By @urregozw


import unittest

class Solution:
    def replaceElements(self, arr: list) -> list:
        mem_p = 0
        for i in range(len(arr) - 1):
            if mem_p <= i: 
                max_num = max(arr[i + 1:])
                mem_p = arr[i + 1:].index(max_num) + i + 1
                arr[i] = max_num
            else:
                arr[i] = arr[mem_p]
        
        arr[len(arr) - 1] = -1
        
        return arr

class TestCase(unittest.TestCase):
    ans = Solution()

    def test_case_1(self):
        query = self.ans.replaceElements([57010,40840,69871,14425,70605])


if __name__ == '__main__':
    unittest.main()    
