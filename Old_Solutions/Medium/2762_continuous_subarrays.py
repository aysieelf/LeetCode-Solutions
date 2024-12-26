"""
Task:
    You are given a 0-indexed integer array nums.
    A subarray of nums is called continuous if:
    Let i, i + 1, ..., j be the indices in the subarray.
    Then, for each pair of indices i <= i1, i2 <= j, 0 <= |nums[i1] - nums[i2]| <= 2.
    Return the total number of continuous subarrays.
    A subarray is a contiguous non-empty sequence of elements within an array.

Topics:
    Sliding Window, Array, Queue, Heap (Priority Queue), Ordered Set, Monotonic Queue,
    Two Pointers, Ordered Map, Hash Table, Dynamic Programming, Binary Search Tree,
    Counting, Segment Tree, Binary Search, Stack, Tree, Memoization, Monotonic Stack,
    Math, Iterator, Recursion, Depth-First Search, Greedy

What I learned:
    Sliding Window Pattern:
        Two pointers (left & right) sliding through array to optimize solution.
        Problem-solving steps:
            left = 0
            for right in range(1, len(nums)+1):
                while not valid: left += 1
                count_subarrays()
    When a window is valid, all its subarrays ending at right pointer are also valid!
    Instead of checking each number pair, use max-min ≤ 2 for the entire window to optimize
"""
from collections import defaultdict


class Solution:
    def continuousSubarrays(self, nums: list[int]) -> int:
        window = defaultdict(int)
        result = 0
        left = 0

        for right in range(len(nums)):
            window[nums[right]] += 1

            while max(window.keys()) - min(window.keys()) > 2:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1

            result += right - left + 1

        return result

sol = Solution()
print(sol.continuousSubarrays([5,4,2,4]))
