"""
Task:
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.

Example:
    [1, 2, 3] = true
    [1, 1, 3] = false

Edge cases:
    [1] = true
"""
from typing import List


# Set Length Comparison
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) == len(nums)

# Early Exit Hash Set
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False