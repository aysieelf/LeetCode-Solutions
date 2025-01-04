"""
Task:
    You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock
    and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Examples:
    [7,1,5,3,6,4] -> 5
    [7,6,4,3,1] -> 0

Edge cases:
    [0] -> 0
    [0, 0, 0, 0, 0] -> 0
    if last number is the smallest number - no need to traverse the whole array
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        min_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            max_profit = max(price - min_price, max_profit)
            if price < min_price:
                min_price = price

        return max_profit


sol = Solution()
prices = [7,1,5,3,6,4]
print(sol.maxProfit(prices))