# 📝 Daily Problem Log

## Problem Information
| Category          | Details                                                                                             |
|-------------------|-----------------------------------------------------------------------------------------------------|
| Date              | 2025 Jan 1                                                                                          |
| Problem Name/Link | [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/description/) |
| Difficulty        | Easy                                                                                                |
| Topic             | Array                                                                                               |
| Pattern Used      | Prefix Sum                                                                                          |

## Time Tracking
| Phase          | Time   |
|----------------|--------|
| Understanding  | 3 min  |
| First Attempt  | 7 min  |
| Solution Study | 2 min  |
| Implementation | 0 min  |
| Total Time     | 12 min |

## Problem Analysis
### What Went Smoothly ✓
- [x] Understanding the problem
- [x] Finding the right approach
- [x] Implementation
- [x] Handling edge cases
- [x] Understanding time complexity
- Details of difficulties encountered:
  - I successfully identified why the first approach was O(n^2) and how to optimize it to O(n) on my own.

### What I Learned
- New concept: Prefix Sum pattern - we keep track of the sum of elements up to the current index to avoid recalculating it every time.
- Mistake to avoid: Avoid slicing the array to calculate the sum of elements up to the current index. It's O(k) time complexity where k is the length of the slice.
- Better approach: Use last element of the result array to calculate the sum of elements up to the current index.

### Performance Rating
- First Try: 🟢
- Understanding: 🟢
- Implementation: 🟢

---