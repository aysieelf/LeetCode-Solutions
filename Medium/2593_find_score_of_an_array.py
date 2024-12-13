"""
Task:
    You are given an array nums consisting of positive integers.

    Starting with score = 0, apply the following algorithm:
        Choose the smallest integer of the array that is not marked. If there is a tie,
        choose the one with the smallest index.
        Add the value of the chosen integer to score.
        Mark the chosen element and its two adjacent elements if they exist.
        Repeat until all the array elements are marked.
        Return the score you get after applying the above algorithm.

Topic:
    Heap (Priority Queue), Sorting, Array, Simulation, Hash Table,
    Ordered Set, Ordered Map, Greedy, Monotonic Stack, Sliding Window,
    Two Pointers, Queue, Stack, Divide and Conquer, Radix Sort,
    Dynamic Programming, Doubly-Linked List, Data Stream, Bit Manipulation,
    Hash Function, Design, Tree, String, Iterator, Counting Sort
"""
from heapq import heapify, heappop


class Solution:
    def findScore(self, nums: list[int]) -> int:
        nums_list = [(nums[i], i) for i in range(len(nums))]
        heapify(nums_list)
        existing = [True] * len(nums)
        existing_count = len(nums)

        result = 0
        while nums_list:
            num, index = heappop(nums_list)

            if existing[index]:
                result += num
                existing[index] = False
                existing_count -= 1
                if index+1 < len(nums) and existing[index+1]:
                    existing[index+1] = False
                    existing_count -= 1
                if index-1 >= 0 and existing[index-1]:
                    existing[index-1] = False
                    existing_count -= 1

            if existing_count == 0:
                break
        return result

sol = Solution()
print(sol.findScore([1247,1847,259,184,637,805,1364,643,1129,1008,1378,554,371,765,1386,1419,1023,1826,845,1941,244,246,1118,981,1779,148,1662,1991,212,1255,47,604,1642,1273,1422,152,1093,4,348,1224,277,126,1551,353,249,1482,56,1590,256,1950,1765,1980,1864,27,77,1520,838,1383,1388,448,870,208,1951,431,411,824,1325,1823,35,3,1330,619]))


