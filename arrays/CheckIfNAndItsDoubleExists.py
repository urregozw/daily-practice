#!/usr/bin/python3

# Exercise 1346 from Leetcode, in the section of arrays
# By @urregozw

import unittest

class Solution:
    def checkIfExist(self, arr: list) -> bool:
        '''
            T.C: O(N)
            S.C: O(1)
        '''
        h = {}
        for i in range(len(arr)):
            num = arr[i]
            if num * 2 in h or num/2 in h:
                return True
            
            h[num] = 1
        
        return False
            


class TestCase(unittest.TestCase):
    ans = Solution()
    def test_case_1(self):
        query = self.ans.checkIfExist([10,2,5,3])
        self.assertEqual(query, True)
        

if __name__ == "__main__":
    unittest.main()
