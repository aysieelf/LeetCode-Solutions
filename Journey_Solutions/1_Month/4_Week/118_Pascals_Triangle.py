"""
Task:
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above.

Example:
    numRows = 5 => [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    numRows = 1 => [[1]]
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]

        for i in range(1, numRows):
            current_row = [1]

            prev_row = result[-1]

            for j in range(1, i):
                current_row.append(prev_row[j - 1] + prev_row[j])

            current_row.append(1)
            result.append(current_row)

        return result

sol = Solution()
numRows = 5
print(sol.generate(numRows))


