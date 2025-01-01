# 🧩 Pattern Library

## Hash Table with Parallel Processing
### Core Concept
- Basic idea: Reducing time complexity in half by checking 
- the complement in the hash table from the beginning and the end of the list at the same time.
- When to use: When we have long lists and we want to reduce time complexity by checking the complement from both ends.
  - I used it in [1_Two_Sum problem](Journey_Solutions/1_Month/1_Week/1_Two_Sum.py)

### Template Code
```python
def hash_table_parallel_processing(nums, target):
    seen = {}  # value -> index
    n = len(nums)
    mid = n // 2
    
    for i in range(mid):
        # Process from start
        curr_start = nums[i]
        if target - curr_start in seen:
            return [seen[target - curr_start], i]
        seen[curr_start] = i
        
        # Process from end
        end_idx = n - 1 - i
        curr_end = nums[end_idx]
        if target - curr_end in seen:
            return [seen[target - curr_end], end_idx]
        seen[curr_end] = end_idx
    
    # Handle middle element for odd length
    if n % 2:
        curr_mid = nums[mid]
        if target - curr_mid in seen:
            return [seen[target - curr_mid], mid]
```
-----
## Hash Map Lookup (Complement Pattern)
### Core Concept
- Basic idea: We use hash map for fast lookup of complementary values
- When to use: When we are looking for pairs of elements that satisfy a certain condition (sum, difference, etc.)
  - I used it in [1_Two_Sum problem](Journey_Solutions/1_Month/1_Week/1_Two_Sum.py)


### Template Code
```python
def hash_map_lookup(arr, target):
    seen = {}  # value : index/info
    
    for i, curr in enumerate(arr):
        complement = target - curr  # or another condition
        
        if complement in seen:
            return [seen[complement], i]  # we found the pair
            
        seen[curr] = i  # we store the current value
    
    return []  # no pair found
```
## Two Pointers
### Core Concept
- Basic idea: We use two pointers to traverse the list from both ends / from back to front / from front to back
- When to use: When we need to compare elements in the list or move them in a certain way
  - [283_Move_Zeroes problem](Journey_Solutions/1_Month/1_Week/283_Move_Zeroes.py)
  - [88_Merge_Sorted_Array problem](Journey_Solutions/1_Month/1_Week/88_Merge_Sorted_Array.py)


### Template Code
```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        # Process elements
        left += 1
        right -= 1
```
