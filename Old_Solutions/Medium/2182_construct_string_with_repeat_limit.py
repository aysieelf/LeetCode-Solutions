"""
Task:
    You are given a string s and an integer repeatLimit.
    Construct a new string repeatLimitedString
    using the characters of s such that no letter appears more than repeatLimit times in a row.
    You do not have to use all characters from s.

    Return the lexicographically largest repeatLimitedString possible.

    A string a is lexicographically larger than a string b
    if in the first position where a and b differ,
    string a has a letter that appears later in the alphabet
    than the corresponding letter in b. If the first min(a.length, b.length)
    characters do not differ, then the longer string is the lexicographically larger one.

Topics:
    Hash Table, String, Greedy, Heap (Priority Queue), Counting

What I learned:
    defaultdict(int) - smart dictionary with auto-zero
    deque - queue with popleft() & append() in python
"""
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        occurrences = defaultdict(int)
        heap = []
        for char in s:
            ascii = ord(char) * -1
            if ascii not in occurrences:
                heappush(heap, ascii)
            occurrences[ascii] += 1

        result = []
        last_char = None
        consecutive_count = 0

        while heap:
            curr_ascii = heappop(heap)
            curr_char = chr(curr_ascii * -1)

            if curr_char == last_char:
                consecutive_count += 1
            else:
                consecutive_count = 1

            if consecutive_count > repeatLimit:
                if not heap:
                    break

                next_ascii = heappop(heap)
                result.append(chr(next_ascii * -1))
                occurrences[next_ascii] -= 1

                if occurrences[next_ascii] > 0:
                    heappush(heap, next_ascii)

                heappush(heap, curr_ascii)

                consecutive_count = 0
                last_char = chr(next_ascii * -1)
                continue

            result.append(curr_char)
            occurrences[curr_ascii] -= 1

            if occurrences[curr_ascii] > 0:
                heappush(heap, curr_ascii)

            last_char = curr_char

        return ''.join(result)

sol = Solution()
print(sol.repeatLimitedString('aababab', 2))