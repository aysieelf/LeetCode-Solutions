"""
Task:
    You are given an integer array nums, an integer k, and an integer multiplier.
    You need to perform k operations on nums. In each operation:

    Find the minimum value x in nums.
    If there are multiple occurrences of the minimum value, select the one that appears first.
    Replace the selected minimum value x with x * multiplier.
    Return an integer array denoting the final state of nums after performing all k operations.


Topics:
    Array, Math, Heap (Priority Queue), Simulation

What I learned:
    When working with an auxiliary data structure (like a heap)
    but needing final results in original order,
    you can modify the output array directly during processing
    instead of reordering at the end.
"""
from heapq import heapify, heappop, heappush

class Solution:
    def getFinalState(self, nums: list[int], k: int, multiplier: int) -> list[int]:
        nums = nums.copy()
        heap = [(n, i) for i, n in enumerate(nums)]
        heapify(heap)

        for _ in range(k):
            num, i = heappop(heap)
            new =  num * multiplier
            nums[i] = new
            heappush(heap, (new, i))

        return nums

sol = Solution()
print(sol.getFinalState([1,3,5,1], 1, 3))