# 📝 Daily Problem Log

## Problem Information
| Category          | Details                                                                                 |
|-------------------|-----------------------------------------------------------------------------------------|
| Date              | 2025 Jan 3                                                                              |
| Problem Name/Link | [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/) |
| Difficulty        | Easy                                                                                    |
| Topic             | Array                                                                                   |
| Pattern Used      | Two Pointers / Sorting                                                                  |

## Time Tracking
| Phase          | Time   |
|----------------|--------|
| Understanding  | 2 min  |
| First Attempt  | 22 min |
| Solution Study | 20 min |
| Implementation | 11 min |
| Total Time     | 55 min |

## Problem Analysis
### What Went Smoothly ✓
- [x] Understanding the problem
- [x] Finding the right approach
- [x] Implementation
- [ ] Handling edge cases
- [ ] Understanding time complexity
- Details of difficulties encountered:
  - I forgot for the edge case where zeroes can be in the middle of the array
  - My solution was not optimal
  - It was hard to find a solution without using insert() method
  - I wasn't sure how to handle the middle zeroes

### What I Learned
- New concept:
  - Tow Pointers technique: using two pointers to traverse the array
  - Moving from back-to-front instead of front-to-back might be more effective
- Mistake to avoid:
  - insert() method has O(n) time complexity and is too slow for this problem
  - choosing hard to understand names for variables (i, j, k)
- Better approach: 
```python
def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    last = m + n - 1  # last element of the merged array
    i1 = m - 1        # last element from nums1
    j2 = n - 1        # last element from nums2
    
    while j2 >= 0:  # while there are elements in nums2
        if i1 < 0 or nums2[j2] >= nums1[i1]: # if nums2 has the bigger element
            nums1[last] = nums2[j2] # put it in the last position
            j2 -= 1
        else:
            nums1[last] = nums1[i1] # put the element from nums1
            i1 -= 1
        last -= 1 # move to the next position
```

### Performance Rating
- First Try: 🟡 (working, but not optimal)
- Understanding: 🟢
- Implementation:  🟡

---