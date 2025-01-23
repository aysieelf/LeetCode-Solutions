"""
Task:
    Given an integer array nums, return the third distinct maximum number in this array.
    If the third maximum does not exist, return the maximum number.

Examples:
    nums = [3,2,1] => 1
    nums = [1,2] => 2
    nums = [2,2,3,1] => 1
"""
from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = float('-inf')

        for num in nums:
            if num in [first, second, third]:
                continue
            elif num > first:
                first, second, third = num, first, second
            elif num > second:
                second, third = num, second
            elif num > third:
                third = num

        return third if third != float('-inf') else first


sol = Solution()
nums = [2,2,3,1]
print(sol.thirdMax(nums))
