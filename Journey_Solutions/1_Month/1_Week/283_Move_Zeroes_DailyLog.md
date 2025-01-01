# 📝 Daily Problem Log

## Problem Information
| Category          | Details                                                                    |
|-------------------|----------------------------------------------------------------------------|
| Date              | 2024 Dec 31                                                                |
| Problem Name/Link | [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/description/) |
| Difficulty        | Easy                                                                       |
| Topic             | Array                                                                      |
| Pattern Used      | Two Pointers                                                               |

## Time Tracking
| Phase          | Time   |
|----------------|--------|
| Understanding  | 2 min  |
| First Attempt  | 12 min |
| Solution Study | 8 min  |
| Implementation | 3 min  |
| Total Time     | 25 min |

## Problem Analysis
### What Went Smoothly ✓
- [x] Understanding the problem
- [x] Finding the right approach
- [x] Implementation
- [x] Handling edge cases
- [x] Understanding time complexity
- Details of difficulties encountered:
  - I had a creative idea to optimize the solution further with a set(), but it didn't work because the numbers might repeat.

### What I Learned
- New concept:
  - Two pointers doesn't always mean from-back-to-front. In this case, it was front-to-back. In this case, I had two pointers pattern, where one pointer was for the last non-zero element and the other was for the current element.
- Mistake to avoid: 
  - I initially thought of using a set() to store the non-zero elements, but that would not work because the numbers might repeat. I shouldn't make assumptions about the input data.
  - I should always be careful about indexes.
- Better approach: 
  - Instead of checking if nums[zero_i] == 0, I could have directly swapped the elements. This would have saved me from writing an extra if condition.
```python
def moveZeroes(self, nums: list[int]) -> None:
    zero_i = 0  # Pointer for the last non-zero element
    
    # For each element, if it's non-zero, swap it with the last non-zero element
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[zero_i], nums[i] = nums[i], nums[zero_i]
            zero_i += 1
```

### Performance Rating
- First Try:  🟢
- Understanding: 🟢
- Implementation: 🟡

---