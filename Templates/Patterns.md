# 🧩 Pattern Library

## Pattern Name: [e.g., Two Pointers]
### Core Concept
- Basic idea: _write here_
- When to use: _write here_

### Template Code
```python
# Basic implementation

```
-----

# 🧩 Pattern Library - EXAMPLE

## Pattern Name: Two Pointers
### Core Concept
- Basic idea: Използваме два указателя които се движат по масива, вместо nested loops
- When to use: Когато търсим двойки елементи или искаме O(n) вместо O(n²)

### Template Code
```python
def two_pointers(arr):
   left = 0
   right = len(arr) - 1
   
   while left < right:
       # Do something
       if CONDITION:
           left += 1
       else:
           right -= 1
   
   return result