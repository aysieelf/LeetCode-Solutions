"""
Task:
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Examples:
    s = "anagram", t = "nagaram" => true
    s = "rat", t = "car" => false
"""
from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = defaultdict(int)
        for l in s:
            seen[l] += 1

        for l in t:
            seen[l] -= 1

        return all(count == 0 for count in seen.values())


sol = Solution()
s = "a"
t = "ab"
print(sol.isAnagram(s, t))
