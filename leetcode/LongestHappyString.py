#!/usr/bin/python3

# Exercise 1405 from Leetcode, in the section of arrays
# By @urregozw

import unittest

class Solution:
    def check_max_values(self, h) -> tuple:
        a, b, c = h["a"], h["b"], h["c"]
        if a >= b and a >= c:
            biggest = "a"
            second_b = "b" if b > c else "c"
        elif b >= a and b >= c:
            biggest = "b"
            second_b = "a" if a > c else "c"
        else:
            biggest = "c"
            second_b = "b" if b > a else "a"

        return biggest, second_b


    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        '''
            T.C: O(a+b+c)
            S.C: O(1)
        '''
        happy = ""
        h = {"a": a, "b": b, "c": c}
        while True:
            biggest, second_b = self.check_max_values(h)
            if len(happy) >= 2:
                sub = happy[-2:]
                if sub == biggest + biggest:
                    if h[second_b] > 0:
                        happy = happy + second_b
                        h[second_b] = h[second_b] - 1
                    else:
                        break
                else:
                    if h[biggest] > 0:
                        happy = happy + biggest
                        h[biggest] = h[biggest] - 1
                    else:
                        break
                
            else:
                if h[biggest] > 0:
                    happy = happy + biggest
                    h[biggest] = h[biggest] - 1
                else:
                    break

        return happy


class TestCase(unittest.TestCase):
    ans = Solution()
    def test_case_1(self):
        query = self.ans.longestDiverseString(a = 1, b = 1, c = 7)
        self.assertEqual(query, "ccaccbcc") # There are multiple solutions, but this one of them
        

if __name__ == "__main__":
    unittest.main()