#!/usr/bin/python3

# Exercise from the day, 10/18/24
# By @urregozw


import itertools
import unittest

class Solution:

    def combinations(self, nums: list, elements: int, target: int) -> int:
        combinations = itertools.combinations(nums, elements)
        count = 0
        for l in combinations:
            total = 0
            for num in l:
                total |= num
            
            if total == target:
                count += 1
        
        return count


    def countMaxOrSubsets(self, nums: list) -> int:
        target = 0
        for num in nums:
            target = target | num
        
        count = 1 # With all the numbers you get 1
        elements = 1
        while len(nums) != elements:
            count += self.combinations(nums, elements, target)
            elements += 1

        return count
        
        

class TestCase(unittest.TestCase):
    ans = Solution()
    def test_case_1(self):
        query = self.ans.countMaxOrSubsets([2,2,2])
        self.assertEqual(query, 7)


if __name__ == '__main__':
    unittest.main()