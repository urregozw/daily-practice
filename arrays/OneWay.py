#!/usr/bin/python3

# Exercise 1.5 from CiCt
# By @urregozw

import unittest

class Solution():

    def put_in_hash(self, s: str) -> dict:
        h = {}
        for letter in s:
            if letter in h:
                h[letter] += 1
            else:
                h[letter] = 1
        
        return h

    def hash_len_equals_1(self, h: dict) -> bool:
        return True if len(h) == 1 else False

    def check_string(self, s: str, h: dict) -> bool:
        for letter in s:
            if letter in h:
                h[letter] -= 1
                if h[letter] == 0: del h[letter]
            else:
                return False
        
        return self.hash_len_equals_1(h)



    def one_way(self, s1: str, s2: str) -> bool:
        """
            We do not take into account the lenght of the string
            because of there will always be one unit of difference
            so it can be put to N, being N the lenght of any of the two string
            T.C: O(N)
            S.C: O(N)
        """
        if s1 == s2: return True
        h = {}

        if len(s1) + 1 == len(s2):
            h = self.put_in_hash(s2)
            return self.check_string(s1, h)        

        elif len(s1) - 1 == len(s2):
            h = self.put_in_hash(s1)
            return self.check_string(s2, h) 

        elif len(s1) == len(s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
            
            return True if count == 1 else False

        else:
            return False

class TestCase(unittest.TestCase):
    ans = Solution()
    def test_case_1(self):
        query = self.ans.one_way("pale", "ple")
        self.assertEqual(query, True)


if __name__ == '__main__':
    unittest.main()