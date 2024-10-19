#!/usr/bin/python3

# Exercise 88 from Leetcode, in the section of arrays
# By @urregozw

import unittest

class Solution:
    def invert(self, s):
        inverted = ""
        for num in s:
            inverted += "0" if num == "1" else "1"

        return inverted

    def findKthBit(self, n: int, k: int) -> str:
        s_base = "0"
        s_n = "0"
        for _ in range(1, n):
            s_n = s_base + "1" + self.invert(s_base)[::-1]
            s_base = s_n
        return s_n[k - 1]
    
class TestCases(unittest.TestCase):
    ans = Solution()

    def test_case_1(self):
        query = self.ans.findKthBit(n = 4, k = 11)
        self.assertEqual(query, "1")

if __name__ == '__main__':
    unittest.main()