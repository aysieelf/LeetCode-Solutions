"""
Task:
    Given an array of integers nums, calculate the pivot index of this array.
    The pivot index is the index where the sum of all the numbers strictly to
    the left of the index is equal to the sum of all the numbers strictly to the index's right.
    If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left.
    This also applies to the right edge of the array.

    Return the leftmost pivot index. If no such index exists, return -1.

Examples:
    [1,7,3,6,5,6] -> 3
    [1,2,3] -> -1
    [2,1,-1] -> 0
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_half = sum(nums)
        left_half = 0

        for i, num in enumerate(nums):
            right_half -= num
            if left_half == right_half:
                return i
            left_half += num

        return -1
