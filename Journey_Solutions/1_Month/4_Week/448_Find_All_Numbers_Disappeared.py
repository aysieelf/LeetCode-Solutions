"""
Task:
    Given an array nums of n integers where nums[i] is in the range [1, n],
    return an array of all the integers in the range [1, n] that do not appear in nums.

Examples:
    nums = [4,3,2,7,8,2,3,1] => [5,6]
    nums = [1,1] => [2]
"""
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_set = set(nums)
        result = []
        for i in range(1, len(nums)+1):
            if i not in nums_set:
                result.append(i)

        return result
