#!/usr/bin/python3

# Exercise 1089 from Leetcode, in the section of arrays
# By @urregozw

import unittest

class Solution:    
    def duplicateZeros(self, arr: list) -> None:
        """
        Do not return anything, modify arr in-place instead.
        
        Time: O(N + N) -> O(2N) -> O(n)
        Space: O(N)
        """
        i = 0
        j = 0
        c_array = arr.copy()
        while i < len(arr):
            num = arr[j]
            if num == 0:
                c_array[i] = 0
                if i + 1 < len(arr):
                    c_array[i + 1] = 0
                i +=1
            else:
                c_array[i] = num
            i +=1
            j += 1
        
        for i in range(len(c_array)):
            arr[i] = c_array[i]
        

        return arr # Just for the tests
        


class TestCases(unittest.TestCase):
    ans = Solution()

    def test_case_1(self):
        query = self.ans.duplicateZeros([1,0,2,3,0,0,0,0])
        self.assertEqual(query, [1,0,0,2,3,0,0,0])


if __name__ == '__main__':
    unittest.main()