# 📝 Daily Problem Log - EXAMPLE

## Problem Information
| Category | Details |
|----------|---------|
| Date | 2024-12-26 |
| Problem Name/Link | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |
| Difficulty | Easy |
| Topic | Binary Tree |
| Pattern Used | DFS (Recursive) |

## Time Tracking
| Phase | Time |
|-------|------|
| Understanding | 5 min |
| First Attempt | 15 min |
| Solution Study | 10 min |
| Implementation | 8 min |
| Total Time | 38 min |

## Problem Analysis
### Difficulties Faced
- [ ] Understanding problem
- [x] Finding approach
- [ ] Implementation 
- [ ] Edge cases
- [ ] Time complexity
- Details: Първоначално се чудех дали да използвам BFS или DFS. Трябваше ми време да осъзная, че с DFS ще е по-елегантно решението.

### What I Learned
- New concept: Height на дърво може да се намери рекурсивно като вземем max от височината на лявото и дясното поддърво + 1
- Mistake to avoid: Не забравяй base case за null node!
- Better approach: DFS е по-чист от BFS за тази задача защото не ни трябва допълнителна памет за queue

### Performance Rating
- First Try: 🟡 
- Understanding: 🟢
- Implementation: 🟢

---