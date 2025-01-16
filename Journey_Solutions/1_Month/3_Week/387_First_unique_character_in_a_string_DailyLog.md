# 📝 Daily Problem Log

## Problem Information
| Category          | Details                                                                                                                  |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|
| Date              | 2025-01-16                                                                                                               |
| Problem Name/Link | [387. First unique character in a string](https://leetcode.com/problems/first-unique-character-in-a-string/description/) |
| Difficulty        | Easy                                                                                                                     |
| Topic             | String                                                                                                                   |
| Pattern Used      | Hash Table                                                                                                               |

## Time Tracking
| Phase          | Time   |
|----------------|--------|
| Understanding  | 2 min  |
| First Attempt  | 7 min  |
| Solution Study | 20 min |
| Implementation | 2 min  |
| Total Time     | 33 min |

## Problem Analysis
### What Went Smoothly ✓
- [x] Understanding the problem
- [x] Finding the right approach
- [x] Implementation
- [x] Handling edge cases
- [ ] Understanding time complexity
- Details of difficulties encountered: I used a built-in function index() to find the index of the first occurrence of a character, but this is O(n) time complexity.

### What I Learned
- New concept: index() is O(n) time complexity, so using a hash table to store the index of each character is more efficient
- Mistake to avoid: Using build-in functions because they may not be the most efficient
- Better approach: I should have used a hash table to store the index of each character to find the first unique character

### Performance Rating
- First Try: 🟢
- Understanding: 🟢
- Implementation: 🟡

LEGEND:
- First Try:
  🟢 - Completed on my own
  🟡 - Used hints
  🔴 - Used solution

- Understanding:
  🟢 - Understood and can explain the problem to others
  🟡 - Understood main idea
  🔴 - Still struggling to understand the problem

- Implementation:
  🟢 - Wrote clean code, no bugs, optimal naming
  🟡 - Wrote code with some bugs, not optimal naming
  🔴 - Many bugs, poor naming, needed help
---