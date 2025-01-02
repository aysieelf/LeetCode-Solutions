"""
Task:
    Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
    Return the running sum of nums.

Examples:
    [1, 4, 3, 1] => [1, 5, 8, 9]

Edge cases:
    [1] => [1]
    [0] => [0]

"""
from typing import List
#
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         return [sum(nums[:i+1]) for i in range(len(nums))]

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for num in nums[1:]:
            result.append(result[-1] + num)

        return result


sol = Solution()
nums = [3,1,2,10,1]
print(sol.runningSum(nums))
