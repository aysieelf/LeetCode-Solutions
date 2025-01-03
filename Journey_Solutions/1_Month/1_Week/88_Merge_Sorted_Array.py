"""
Task:
    You are given two integer arrays nums1 and nums2,
    sorted in non-decreasing order, and two integers m and n,
    representing the number of elements in nums1 and nums2 respectively.

    Merge nums1 and nums2 into a single array sorted in non-decreasing order.
    The final sorted array should not be returned by the function,
    but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n,
    where the first m elements denote the elements that should be merged,
    and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        i1 = m - 1
        j2 = n - 1

        while j2 >= 0:
            if i1 < 0 or nums2[j2] >= nums1[i1]:
                nums1[last] = nums2[j2]
                j2 -= 1
            else:
                nums1[last] = nums1[i1]
                i1 -= 1

            last -= 1


sol = Solution()
nums1 = [1,2,3,0,0,0]
sol.merge(nums1, 3, [2,5,6], 3)
print(nums1)
