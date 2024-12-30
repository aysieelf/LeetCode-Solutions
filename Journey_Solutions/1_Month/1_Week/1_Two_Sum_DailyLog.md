# 📝 Daily Problem Log

## Problem Information
| Category          | Details                                                          |
|-------------------|------------------------------------------------------------------|
| Date              | 2024 Dec 30                                                      |
| Problem Name/Link | [1. Two Sum](https://leetcode.com/problems/two-sum/description/) |
| Difficulty        | Easy                                                             |
| Topic             | Array / Hash Table                                               |
| Pattern Used      | Hash Table with Parallel Processing                              |

## Time Tracking
| Phase          | Time   |
|----------------|--------|
| Understanding  | 5 min  |
| First Attempt  | 15 min |
| Solution Study | 12 min |
| Implementation | 3 min  |
| Total Time     | 35 min |

## Problem Analysis
### What Went Smoothly ✓
- [x] Understanding the problem
- [x] Finding the right approach
- [x] Implementation
- [ ] Handling edge cases
- [ ] Understanding time complexity
- Details of difficulties encountered:
  - Wasn't sure how to determine time and space complexity
  - Struggled with naming the hash table
  - Forgot for the case where len(nums) % 2 == 1

### What I Learned
- New concept:
  - Time complexity of O(n/2) is still O(n)
  - Hash Table with Parallel Processing pattern - new approach to optimize time complexity
  - Using a hash table for O(1) lookup time
- Mistake to avoid: 
  - Didn't need to use the parallel processing approach, although it was a good learning experience and made the code slightly faster
  - I didn't need to return an empty list at the end, because of the constraints
- Better approach:
  - enumerate would make the code cleaner
  - seen is a better name for the hash table

### Performance Rating
- First Try: 🟢
- Understanding: 🟢
- Implementation: 🟡

---