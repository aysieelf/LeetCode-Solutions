"""
Task:
    You are given an integer array gifts denoting the number of gifts in various piles.
    Every second, you do the following:
        Choose the pile with the maximum number of gifts.
        If there is more than one pile with the maximum number of gifts, choose any.
        Leave behind the floor of the square root of the number of gifts in the pile.
        Take the rest of the gifts.
        Return the number of gifts remaining after k seconds.

Topic:
    Array, Heap (Priority Queue), Simulation

What I learned:
   - Heap is a tree-based structure where parent node is always bigger than child nodes;
   - Heapq methods: heapify (list->heap), heappush (add), heappop (remove root);
   - Python uses Min Heap by default, so we use negative numbers for Max Heap;
"""
import math
from heapq import heappop, heappush, heapify


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        heap = list(map(lambda x: - x, gifts))
        heapify(heap)

        for _ in range(k):
            max_heap = - heappop(heap)
            left_behind = - math.floor(math.sqrt(max_heap))
            heappush(heap, left_behind)

        return - sum(heap)

sol = Solution()
print(sol.pickGifts([25,64,9,4,100], 4))

