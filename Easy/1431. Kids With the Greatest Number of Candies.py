# 🧩 Problem: LeetCode 1431 – Kids With the Greatest Number of Candies
# You are given an integer array candies, where each element represents
# the number of candies a kid has, and an integer extraCandies.
# Return a boolean array where each value indicates whether the kid can
# have the greatest number of candies after receiving extraCandies.

# 🍀 Approach:
# - Find the maximum number of candies among all kids.
# - Initialize an empty list to store boolean results.
# - Iterate through each kid’s candies.
# - For each kid, check if their candies plus extraCandies is greater than or equal to the maximum.
# - Append True or False accordingly to the result list.
# - Return the final list.

# ⚠️ Disclaimer:
# This is my approach and there might be better approaches out there.
# The code snippet given is after my answer was accepted in LeetCode.

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_c = max(candies)
        li = []
        for i in range(len(candies)):
            if candies[i]+extraCandies >= max_c:
                li.append(True)
            else:
                li.append(False)
        return li