#!/usr/bin/python3

# Exercise from the day, 10/25/24
# By @urregozw

import unittest


class Solution:
    def removeSubfolders(self, folder: list) -> list:
        folder = sorted(folder, key=len)
        subfolders = set()
        i = 0 
        while i < len(folder):
            subfolder = folder[i]
            found = False

            while subfolder != "":
                index = subfolder.rfind("/")
                prefix = subfolder[:index]

                if prefix in subfolders:
                    found = True
                    break
                else:
                    subfolder = subfolder[:index]
            
            if found:
                folder.pop(i)
            else:
                subfolder = folder[i]
                subfolders.add(subfolder)
                i += 1

        
        return folder

                


class TestCases(unittest.TestCase):
    ans = Solution()

    def test_case_1(self):
        query = self.ans.removeSubfolders(folder=["/a","/a/b","/c/d","/c/d/e","/c/f"])
        self.assertEqual(query, ["/a","/c/d","/c/f"])


if __name__ == '__main__':
    unittest.main()
