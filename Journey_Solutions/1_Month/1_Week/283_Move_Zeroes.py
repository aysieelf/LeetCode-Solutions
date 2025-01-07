"""
Task:
    Given an integer array nums, move all 0's to the end of it
    while maintaining the relative order of the non-zero elements.
    Note that you must do this in-place without making a copy of the array.

Edge cases:
    [0, 0, 0, 0, 0]
    []
    [0, 0, 0, 1, 2]
    [0]
    [1]
    [1, 0, 0, 0, 0]
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_i = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero_i], nums[i] = nums[i], nums[zero_i]
                zero_i += 1



sol = Solution()
nums = [1,0,1]
sol.moveZeroes(nums)
print(nums)
