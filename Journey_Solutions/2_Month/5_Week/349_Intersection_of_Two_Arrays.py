"""
Task:
    Given two integer arrays nums1 and nums2, return an array of their intersection.
    Each element in the result must be unique, and you may return the result in any order.

Examples:
    nums1 = [1,2,2,1], nums2 = [2,2] => [2]
    nums1 = [4,9,5], nums2 = [9,4,9,8,4] => [9,4] or [4,9]

Edge Cases:
    nums1 = [1,2,3,4], nums2 = [5,6,7,8] => []
    nums1 = [1,2,3,4], nums2 = [1,2,3,4] => [1,2,3,4]
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        set1 = set(nums1)
        return list(set1.intersection(set(nums2)))