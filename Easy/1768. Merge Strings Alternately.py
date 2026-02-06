# 🧩 Problem: LeetCode 1768 – Merge Strings Alternately
# Given two strings `word1` and `word2`, merge them by adding characters
# alternately starting from `word1`. If one string is longer, append the
# remaining characters at the end.

# 🍀 Approach:
# - Initialize an empty string `merge` to store the final result.
# - Use a loop that runs till the length of the shorter string.
# - In each iteration, append one character from `word1` and one from `word2`.
# - Keep track of the index using a variable.
# - After the loop, append the remaining part of the longer string.
# - Return the merged string.

# ⚠️ Disclaimer:
# This is my approach and there might be better approaches out there.
# The code snippet given is after my answer was accepted in LeetCode.

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        j=0
        for i in range(min(len(word1),len(word2))):
            merge+=word1[i]
            merge+=word2[i]
            j+=1
        if len(word1)>j:
            merge+=word1[j:]
        else:
            merge+=word2[j:]
        return merge  