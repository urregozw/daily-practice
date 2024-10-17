#!/usr/bin/python3

# Exercise 670 from Leetcode, the exercise of the day 10/17/24
# By @urregozw

import unittest

class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        found = False
        
        for i in range(len(num)):
            biggest = num[i]
            position = len(num) - 1
            
            for j in range(len(num) - 1, i, -1):
                challenger = num[j]
                if challenger > biggest:
                    biggest = num[j]
                    position = j
                    found = True

            if found: 
                num[position], num[i] = num[i], num[position]
                break
        
        return int(''.join(num))

class TestCase(unittest.TestCase):
    ans = Solution()

    def test_case_1(self):
        query = self.ans.maximumSwap(num=98368)
        self.assertEqual(query, 98863)

if __name__ == "__main__":
    unittest.main()


