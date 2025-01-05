"""
Task:
    Given an array nums of size n, return the majority element.
    The majority element is the element that appears more than ⌊n / 2⌋ times.
    You may assume that the majority element always exists in the array.
    Follow-up: Could you solve the problem in linear time and in O(1) space?

Examples:
    [3, 2, 3] => 3
    [2, 2, 1, 1, 1, 2, 2] => 2

Edge cases:
    [1, 1, 1, 1, 1, ... 1] => if first and last el are the same?
"""
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        len_n = len(nums)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if count[num] > len_n / 2:
                return num

    def boyer_moore(self, nums):
        candidate = nums[0]
        count = 1
        for num in nums[1:]:
            if num == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = num
                    count += 1

        return candidate

sol = Solution()
nums = [3,2,3]
print(sol.boyer_moore(nums))


