"""
Task:
    Given a pattern and a string s, find if s follows the same pattern.
    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
    Specifically:
        Each letter in pattern maps to exactly one unique word in s.
        Each unique word in s maps to exactly one letter in pattern.
        No two letters map to the same word, and no two words map to the same letter.

Examples:
    pattern = "abba", s = "dog cat cat dog" => True
    pattern = "abba", s = "dog cat cat fish" => False
    pattern = "aaaa", s = "dog cat cat dog" => False
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_word = {}
        word_to_pattern = {}

        words = s.split()
        if len(words) != len(pattern):
            return False

        for char, word in zip(pattern, words):
            if char in pattern_to_word:
                if pattern_to_word[char] != word:
                    return False
            elif word in word_to_pattern:
                if word_to_pattern[word] != char:
                    return False
            else:
                pattern_to_word[char] = word
                word_to_pattern[word] = char

        return True

sol = Solution()
pattern = "abba"
s = "dog dog dog dog"
print(sol.wordPattern(pattern, s))

