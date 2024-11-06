#!/usr/bin/python3

# Exercise 1.4 from CtCi
# By @urregozw

import unittest

class Solution:

    @staticmethod
    def palindrome_permutation(s: str) -> bool:
        """
            T.C: O(N)
            S.C: O(N)
        """
        h = {}
        s = s.lower().replace(" ", "")
        for l in s:
            if l in h:
                del h[l]
            else:
                h[l] = 1
        
        if len(h) <= 1:
            return True
        
        return False

class TestCase(unittest.TestCase):
    def test_case_1(self):
        query = Solution.palindrome_permutation(s="Taco Cat")
        self.assertEquals(query, True)


if __name__ == "__main__":
    unittest.main()