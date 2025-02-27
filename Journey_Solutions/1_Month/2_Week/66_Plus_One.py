"""
Task:
    You are given a large integer represented as an integer array digits,
    where each digits[i] is the ith digit of the integer.
    The digits are ordered from most significant to the least significant in left-to-right order.
    The large integer does not contain any leading 0's.

    Increment the large integer by one and return the resulting array of digits.

Examples:
    [1, 0] => [1, 1]

Edge Cases:
    [1, 9, 9] => [2, 0, 0]
"""
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

            if i == 0:
                digits.insert(0, 1)
                return digits

sol = Solution()
digits = [9]
print(sol.plusOne(digits))
