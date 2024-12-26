"""
Task:
    You are given an integer array prices where prices[i] is the price of the ith item in a shop.
    There is a special discount for items in the shop.
    If you buy the ith item, then you will receive a discount equivalent to prices[j]
    where j is the minimum index such that j > i and prices[j] <= prices[i].
    Otherwise, you will not receive any discount at all.

    Return an integer array answer where answer[i] is the final
    price you will pay for the ith item of the shop, considering the special discount.

Topics:
    Array, Stack, Monotonic Stack

What I learned:
    Monotonic stack is useful for finding "next smaller/greater element" problems
    Traversing array from end to start (reverse) makes solution cleaner
    In monotonic stack pattern: pop elements until we find the right position for current element
"""

class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stack = []

        for i in range(len(prices)-1, -1, -1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            new_price = prices[i]
            if stack and prices[i] >= stack[-1]:
                new_price = prices[i] - stack[-1]


            stack.append(prices[i])
            if new_price != prices[i]:
                prices[i] = new_price

        return prices

sol = Solution()
print(sol.finalPrices([10,1,1,6]))