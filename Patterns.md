# 🧩 Pattern Library

## Table of Contents
- [Hash Table with Parallel Processing](#hash-table-with-parallel-processing)
- [Hash Map Lookup (Complement Pattern)](#hash-map-lookup-complement-pattern)
- [Two Pointers](#two-pointers)
- [Prefix Sum](#prefix-sum)
- [Hash Set](#hash-set)
- [Sorted Array](#sorted-array)

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
---

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
-----
## Prefix Sum
### Core Concept
- Basic idea: We keep track of the sum of elements up to the current index to avoid recalculating it every time
- When to use: 
  - When we need to calculate the sum of elements up to the current index multiple times
  - When we need a sum of subarray from index i to j
  - I used it in [1480_Running_Sum problem](Journey_Solutions/1_Month/1_Week/1480_Running_Sum_of_1d_Array.py)

### Template Code
```python
def prefix_sum(arr):
    prefix = [arr[0]]  # Initialize with first element
    
    for num in arr[1:]:
        # Add current number to previous sum
        prefix.append(prefix[-1] + num)
    
    return prefix

# Alternative one-liner using accumulate
from itertools import accumulate
def prefix_sum_oneliner(arr):
    return list(accumulate(arr))
```
-----
## Hash Set
### Core Concept
- Basic idea: Using a hash set for O(1) lookup time operations
- When to use: When searching for duplicates, membership testing, or maintaining unique elements
  - I used it in [217_Contains_Duplicate problem](Journey_Solutions/1_Month/1_Week/217_Contains_Duplicate.py)

### Template Code
```python
# Approach 1: Set Length Comparison
def has_duplicates_set_comparison(arr):
    return len(set(arr)) != len(arr)

# Approach 2: Early Exit Hash Set
def has_duplicates_early_exit(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return True
        seen.add(num)
    return False
```
-----
## Sorted Array
### Core Concept
- Basic idea: Sorting the array to bring similar elements together
- When to use: When **space complexity** is a concern and O(n log n) time is acceptable

### Template Code
```python
def has_duplicates_sorting(arr):
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return True
    return False
```
-----