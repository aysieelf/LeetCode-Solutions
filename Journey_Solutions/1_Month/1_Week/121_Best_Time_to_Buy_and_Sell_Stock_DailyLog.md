# 📝 Daily Problem Log

## Problem Information
| Category          | Details                                                                                                            |
|-------------------|--------------------------------------------------------------------------------------------------------------------|
| Date              | 2025 Jan 4                                                                                                         |
| Problem Name/Link | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/) |
| Difficulty        | Easy                                                                                                               |
| Topic             | Array                                                                                                              |
| Pattern Used      | Dynamic Programming (State Tracking)                                                                               |

## Time Tracking
| Phase          | Time   |
|----------------|--------|
| Understanding  | 3 min  |
| First Attempt  | 30 min |
| Solution Study | 10 min |
| Implementation | 3 min  |
| Total Time     | 46 min |

## Problem Analysis
### What Went Smoothly ✓
- [x] Understanding the problem
- [ ] Finding the right approach
- [x] Implementation
- [x] Handling edge cases
- [x] Understanding time complexity
- Details of difficulties encountered:
  - Initially tried using nested loops which was O(n²)
  - Tried to track both max and min with indices which was overcomplicated 
  - Needed help to understand the DP approach

### What I Learned
- New concept: Dynamic Programming (State Tracking) - (min_price, max_profit) instead of tracking all data
- Mistake to avoid: Don't overcomplicate by tracking indices when unnecessary
- Better approach: 
  - Process data sequentially while maintaining minimal state
  - In Python, if/else can be faster than min/max functions
  - The order of operations can affect performance

### Performance Rating
- First Try: 🔴
- Understanding: 🟢
- Implementation: 🟢

---