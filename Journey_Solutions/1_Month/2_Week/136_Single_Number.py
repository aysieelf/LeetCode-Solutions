"""
Task:
    Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
    You must implement a solution with a linear runtime complexity and use only constant extra space.

Examples:
    nums = [2,2,1] => 1
    [4,1,2,1,2] => 4
    [1] => 1

Edge cases:
    [1, 1, 2, 2, 3] => 3
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)

        return seen.pop()

    def single_number_xor(self, nums):
        result = 0
        for num in nums:
            result ^= num

        return result
