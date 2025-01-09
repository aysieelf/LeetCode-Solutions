"""
Task:
    Given a sorted array of distinct integers and a target value,
    return the index if the target is found.
    If not, return the index where it would be if it were inserted in order.

    You must write an algorithm with O(log n) runtime complexity.

Examples:
    nums = [1,3,5,6], target = 5 => 2
    nums = [1,3,5,6], target = 2 => 1
    nums = [1,3,5,6], target = 7 => 4
"""


class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1

        return left

sol = Solution()
nums = [1,3,5,6]
t = 7
print(sol.searchInsert(nums, t))





