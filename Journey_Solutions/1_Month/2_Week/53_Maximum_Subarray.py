"""
Task:
    Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example:
    [-2,1,-3,4,-1,2,1,-5,4] => [4,-1,2,1] => 6

"""
from typing import List

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = float('-inf')
#         span = len(nums)
#         while span > 0:
#             for i in range(0, len(nums)):
#                 l = i + span
#                 if l <= len(nums):
#                     curr_sum = sum(nums[i: l])
#                     max_sum = max(max_sum, curr_sum)
#             span -= 1
#         return max_sum


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        max_sum = float('-inf')
        for num in nums:
            if current_sum + num > num:
                current_sum += num
            else:
                current_sum = num

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


sol = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(sol.maxSubArray(nums))


