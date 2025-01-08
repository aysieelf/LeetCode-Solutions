"""
Task:
    Given an integer array nums sorted in non-decreasing order,
    remove the duplicates in-place such that each unique element appears only once.
    The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

    Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
        Change the array nums such that the first k elements of nums contain
        the unique elements in the order they were present in nums initially.
        The remaining elements of nums are not important as well as the size of nums.
        Return k.

Examples:
    [1, 1, 2] => 2, [1, 2, _]
    [0,0,1,1,1,2,2,3,3,4] => 5, [0,1,2,3,4,_,_,_,_,_]

Edge cases:
    [0, 1, 1, 1, 1, 2]
    [0]
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1
