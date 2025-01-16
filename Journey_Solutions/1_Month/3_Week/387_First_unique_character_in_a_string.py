"""
Task:
    Given a string s, find the first non-repeating character
    in it and return its index. If it does not exist, return -1.

Example:
    s = "leetcode" => 0
    s = "aabb" => -1
"""
from collections import defaultdict, deque, Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i, c in enumerate(s):
            if c in seen:
                seen[c] = -1
            else:
                seen[c] = i

        for v in seen.values():
            if v != -1:
                return v

        return - 1



sol = Solution()
s = "loveleetcode"
print(sol.firstUniqChar(s))