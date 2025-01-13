# 🧩 Pattern Library

## Table of Contents
- [Hash Table with Parallel Processing](#hash-table-with-parallel-processing)
- [Hash Map Lookup (Complement Pattern)](#hash-map-lookup-complement-pattern)
- [Two Pointers](#two-pointers)
- [Prefix Sum](#prefix-sum)
- [Hash Set](#hash-set)
- [Sorted Array](#sorted-array)
- [Dynamic Programming (State Tracking)](#dynamic-programming-state-tracking)
- [Boyer-Moore Voting Algorithm](#boyer-moore-voting-algorithm)
- [Hash Table/Hash Map](#hash-tablehash-map)

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

## Dynamic Programming (State Tracking)
### Core Concept
- Basic idea: Track minimum state needed to solve the problem without storing all data
- When to use:
  - When we need to track optimal values while processing data sequentially
  - When we can make decisions based only on previously calculated results
  - I used it in [121_Best_Time_to_Buy_and_Sell_Stock problem](Journey_Solutions/1_Month/1_Week/121_Best_Time_to_Buy_and_Sell_Stock.py)

### Template Code
```python
def dp_state_tracking(arr):
    if not arr: return 0
    
    # Initialize state variables
    min_seen = arr[0]    # Track minimum value seen
    max_result = 0       # Track optimal result
    
    # Process array sequentially
    for num in arr[1:]:
        # Update result using current state
        max_result = max(num - min_seen, max_result)
        # Update state for next iteration
        min_seen = min(min_seen, num)
    
    return max_result
```
-----
## Boyer-Moore Voting Algorithm
### Core Concept
- Basic idea: We maintain a count and a candidate, and we decrease/increase them based on certain conditions
- When to use: When we need to find the majority element in an array (appears more than n/2 times)
  - I used it in [169_Majority_Element problem](Journey_Solutions/1_Month/1_Week/169_Majority_Element.py)

### Template
```python
def boyer_moore_voting(arr):
    candidate = arr[0]
    count = 1
    
    # Process array using voting system
    for num in arr[1:]:
        if num == candidate:
            count += 1
        else:
            count -= 1
            if count == 0:
                candidate = num
                count = 1
    
    return candidate
```
-----
## Kadane's Algorithm (Dynamic Programming)
### Core Concept
- Basic idea: We keep track of the maximum subarray sum ending at the current index
- When to use: When we need to find the maximum subarray sum in an array
  - I used it in [53_Maximum_Subarray problem](Journey_Solutions/1_Month/2_Week/53_Maximum_Subarray.py)
  - Perfect for problems involving contiguous sequences where we need to optimize some value

### Template
```python
def kadanes_algorithm(arr):
    current_sum = 0
    max_sum = float('-inf')
    
    for num in arr:
        # Decide: continue current subarray or start new one
        if current_sum + num > num:
            current_sum += num
        else:
            current_sum = num
            
        # Update global maximum if needed
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum
```
-----
## Binary Search
### Core Concept
- Basic idea: Search for an element in a sorted array by repeatedly dividing the search space in half
- When to use:
  - When the array is sorted
  - When searching for a specific value
  - When we need O(log n) instead of O(n)
  - Finding insertion points in sorted arrays
  - I used it in [35_Search_Insert_Position problem](Journey_Solutions/1_Month/2_Week/35_Search_Insert_Position.py)

### Template
```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Important: integer division
        
        if arr[mid] == target:
            return mid            # We found the target
        elif arr[mid] < target:
            left = mid + 1        # Search in right half
        else:
            right = mid - 1       # Search in left half
    
    return left  # For insertion point
```
-----
## Bit Manipulation (XOR - Exclusive OR)
### Core Concept
- Basic idea: XOR operations track unique elements by automatically canceling out duplicates - when the same number is encountered twice, it's removed from the result
- When to use:
  - When we need to find unique elements with constant space complexity
  - When dealing with duplicate removal problems where each element appears exactly twice, except for one
  - Example: Used in [136. Single Number](Journey_Solutions/1_Month/2_Week/136_Single_Number.py)

### Template Code
```python
def xor_operator(nums):
    result = 0
    # XOR all numbers - duplicates will cancel out
    for num in nums:
        result ^= num  # XOR operation: a^a = 0, a^0 = a
    
    return result  # The remaining value is the unique element
```
-----
## Hash Table/Hash Map

### Core Concept
- Basic idea: We use hash table за O(1) lookup instead of O(n) searching или O(n log n) sorting
- When to use: 
  - When searching for frequency of elements
  - When searching for pairs of elements with a specific relationship
  - For checking if an element exists
  - For counting problems

### Template Code
```python
from collections import defaultdict

def hash_table_pattern(arr):
    # Using defaultdict to avoid key errors
    count = defaultdict(int)
    
    # Count frequencies
    for x in arr:
        count[x] += 1
    
    # Check frequencies or find pairs
    for x in arr:
        if CONDITION:
            # Do something
            pass
    
    return result
```
---