"""
Task:
    There is a school that has classes of students and each class will be having a final exam.
    You are given a 2D integer array classes, where classes[i] = [pass i, total i].
    You know beforehand that in the ith class,
    there are total i total students,
    but only pass i number of students will pass the exam.

    You are also given an integer extraStudents.
    There are another extraStudents brilliant students
    that are guaranteed to pass the exam of any class they are assigned to.
    You want to assign each of the extraStudents students
    to a class in a way that maximizes the average pass ratio across all the classes.

    The pass ratio of a class is equal to the number of students
    of the class that will pass the exam divided by the total number of students of the class.
    The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.

    Return the maximum possible average pass ratio after assigning the extraStudents students.
    Answers within 10-5 of the actual answer will be accepted.

Topics:
    Array, Greedy, Heap (Priority Queue)

What I learned:
   Heaps:
       Sort by first element in tuple
       For max heap use negative values
       O(log n) complexity for finding max/min

   Numbers Precision:
       Float operations cause rounding errors
       Memoization with floats accumulates errors
       Better avoid storing intermediate float results

   Optimization:
       Heap operations O(log n) vs list iteration O(n)
       Work directly with numbers when possible
"""
from heapq import heappush, heappop

class Solution:
    def maxAverageRatio(self, classes: list[list[int]], extraStudents: int) -> float:
        def find_difference(s1: int, s2: int) -> float:
            old = s1 / s2
            new = (s1+1) / (s2+1)
            return new - old

        heap = []
        for s1, s2 in classes:
            heappush(heap, (-find_difference(s1, s2), s1, s2))

        for _ in range(extraStudents):
            _, s1, s2 = heappop(heap)
            s1, s2 = s1 + 1, s2 + 1
            heappush(heap, (-find_difference(s1, s2), s1, s2))

        result = sum(s1 / s2 for r, s1, s2 in heap) / len(heap)

        return result

sol = Solution()
print(sol.maxAverageRatio(classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4))
