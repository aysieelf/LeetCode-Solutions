"""
Task:
    Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example:
    s = "aba" => True
    s = "abca" => True
    s = "abc" => False
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                first_case = s[l+1:r+1]
                second_case = s[l:r]

                return (first_case == first_case[::-1]) or (second_case == second_case[::-1])

            l += 1
            r -= 1
        return True

sol = Solution()
s = "deeee"
print(sol.validPalindrome(s))