# 🔍 Problem: Two Sum (Leetcode #1)
# 💡 Approach:
# - Initialize an empty hash map to store visited numbers and their indices.
# - For each number in the list:
#   - Calculate the difference `sub = target - current number`
#   - Check if this difference exists in the map:
#       - If yes, return [current index, index of the complement]
#       - If not, store the current number and its index in the map
# - This ensures a single-pass solution using hash lookups.
# - Time Complexity: O(n)
# - Space Complexity: O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map1={}
        sub = 0
        for i in range(len(nums)):
            sub=target-nums[i]
            if sub in map1.keys():
                return [i,map1[sub]]
            else:
                map1[nums[i]]=i

# ⚠️ Note:
# This solution follows Leetcode's default class structure.
# It may not run directly in a local IDE without modifying it.