# 📌 Problem: Leetcode 242 – Valid Anagram
# Given two strings `s` and `t`, return `True` if `t` is an anagram of `s`, and `False` otherwise.
# An anagram uses the same characters in any order with the same frequency.

# 🧠 Approach:
# - Create two empty dictionaries `dict1` and `dict2`.
# - Loop through the first string `s`:
#   - For each character, increment its count in `dict1`.
# - Loop through the second string `t`:
#   - For each character, increment its count in `dict2`.
# - Finally, compare both dictionaries.
#   - If they are equal, return `True` (it's an anagram).
#   - Otherwise, return `False`.

# 💬 Personal Note:
# This solution is part of my Python + Leetcode grind series.
# Some Leetcode-specific structures may not work directly in a normal IDE without modification.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        for i in t:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1
        return dict1 == dict2