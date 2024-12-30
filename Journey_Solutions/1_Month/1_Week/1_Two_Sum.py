"""
Task:
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution,
     and you may not use the same element twice.

    You can return the answer in any order.

Edge cases:
- what if no indices exist?
-> no, there is a constraint about that

what if two combinations are correct?
-> no, there is a constraint about that

what if the answer is at the end of a very long list?
-> maybe I should go from two ends to the middle
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        n = len(nums)
        mid = n // 2

        for i in range(mid):
            curr_start = nums[i]
            if target - curr_start in seen:
                return [seen[target - curr_start], i]
            seen[curr_start] = i

            end_idx = n - i - 1
            curr_end = nums[-i-1]
            if target - curr_end in seen:
                return [seen[target - curr_end], end_idx]
            seen[curr_end] = end_idx

        if n % 2 == 1:
            curr_mid = nums[mid]
            if target - curr_mid in seen:
                return sorted([seen[target - curr_mid], mid])


sol = Solution()
print(sol.twoSum([2,7,11,15], 9))
print(sol.twoSum([3,2,4], 6))