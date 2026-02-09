# Note to myself - Missed two days but am continuing with this misses and will try to be consistent, learn to be responsible

# 🧩 Problem: LeetCode 1071 – Greatest Common Divisor of Strings
# Given two strings str1 and str2, return the largest string that divides
# both strings. If there is no such string, return an empty string.

# 🍀 Approach:
# - First, check if concatenating str1 + str2 is equal to str2 + str1.
# - If they are not equal, return an empty string since no common divisor exists.
# - Compute the GCD of the lengths of str1 and str2.
# - Initialize an empty string to store the result.
# - Iterate up to the GCD length and build the result using characters from str1.
# - Return the constructed string.

# ⚠️ Disclaimer:
# This is my approach and there might be better approaches out there.
# The code snippet given is after my answer was accepted in LeetCode.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2 != str2+str1:
            return ""
        g = gcd(len(str1),len(str2))
        s = ""
        for i in range(g):
            s += str1[i]
        return s 