"""
Task:
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above.

Examples:
    3 => [1, 3, 3, 1]
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)

        for i in range(1, rowIndex + 1):
            prev = 1
            for j in range(1, i):
                temp = row[j]
                row[j] = prev + row[j]
                prev = temp

        return row

sol = Solution()
print(sol.getRow(3))