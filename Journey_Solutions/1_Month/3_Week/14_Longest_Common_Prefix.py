"""
Task:
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

Examples:
    strs = ["flower","flow","flight"] => "fl"
    strs = ["dog","racecar","car"] => ""
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        shortest = min(len(s) for s in strs)

        for i in range(shortest):
            char = strs[0][i]

            if not all(s[i] == char for s in strs):
                return strs[0][:i]

        return strs[0][:shortest]


sol = Solution()
strs = ["ab", "a"]
print(sol.longestCommonPrefix(strs))