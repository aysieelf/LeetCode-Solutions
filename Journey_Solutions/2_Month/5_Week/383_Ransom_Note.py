"""
Task:
    Given two stings ransomNote and magazine,
    return true if ransomNote can be constructed from magazine and false otherwise.
    Each letter in magazine can only be used once in ransomNote.

Examples:
    Input: ransomNote = "a", magazine = "b" => Output: false
    Input: ransomNote = "aa", magazine = "ab" => Output: false
    Input: ransomNote = "aa", magazine = "aab" => Output: true
"""
from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        letters = defaultdict(int)
        for letter in magazine:
            letters[letter] += 1

        for letter in ransomNote:
            letters[letter] -= 1
            if letters[letter] < 0:
                return False

        return True