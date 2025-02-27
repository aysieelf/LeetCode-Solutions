"""
Task:
    Write a function that reverses a string. The input string is given as an array of characters s.
    You must do this by modifying the input array in-place with O(1) extra memory.

Examples:
    s = ["h","e","l","l","o"] => ["o","l","l","e","h"]

Edge Cases:
    s = ["e"] => ["e"]

"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]

sol = Solution()
s = ["o","l", "l", "e","h"]
print(sol.reverseString(s))
print(s)