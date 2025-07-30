# Problem: Leetcode 219 – Contains Duplicate II
# Given an array of integers `nums` and an integer `k`, return True if there are two distinct indices i and j
# such that nums[i] == nums[j] and the absolute difference between i and j is at most k. Otherwise, return False.

# 🧠 Approach:
# - Initialize an empty dictionary to track the last seen index of each number.
# - Iterate through the array with index `i`:
#     - If nums[i] already exists in the dictionary:
#         - Check if the current index and stored index have a difference <= k.
#         - If yes, return True.
#     - Update the dictionary with the current index for nums[i], whether or not a match was found.
# - If loop completes without returning True, return False.

# ⚠️ Disclaimer:
# This solution is written specifically for Leetcode's platform and uses their function signature and structure.
# It may require slight modifications to work in a regular Python environment.


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map1 = {}
        for i in range(len(nums)):
            if nums[i] in map1.keys():
                if abs(i-map1[nums[i]])<=k:
                    return True
            map1[nums[i]]=i
        return False