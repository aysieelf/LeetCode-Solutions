"""
Task:
    Given a string s consisting of words and spaces, return the length of the last word in the string.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_word = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ': len_word += 1
            elif len_word != 0: break

        return len_word



sol = Solution()
s = 'a'
print(sol.lengthOfLastWord(s))