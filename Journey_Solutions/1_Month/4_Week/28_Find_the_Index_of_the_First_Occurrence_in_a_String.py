"""
Task:
    Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.

Example:
    haystack = "sadbutsad", needle = "sad" => 0
    haystack = "leetcode", needle = "leeto" => -1
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

sol = Solution()
haystack = "mississippi"
needle = "issip"
print(sol.strStr(haystack, needle))