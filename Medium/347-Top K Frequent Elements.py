# 📌 Problem: Leetcode 347 – Top K Frequent Elements
# Given a list of integers `nums` and an integer `k`, return the `k` most frequent elements.
# The result can be in any order.

# 🧠 Approach:
# - First, create a frequency dictionary using `.get()` to count occurrences.
# - Convert the dictionary into a list of [frequency, number] pairs.
# - Sort the list by frequency (ascending).
# - Pop the last `k` elements from the list (they have highest frequency).
# - Extract the number from each and return the result list.

# 💬 Personal Note:
# This code is part of my Python grind + Leetcode journey.
# Some Leetcode-only functions/structures may not work directly in a normal IDE without modification.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic1 = {}
        list1 = []
        result = []

        for i in nums:
            dic1[i] = 1+ dic1.get(i,0)

        for a,b in dic1.items():
            list1.append([b, a])
        list1.sort(reverse=True)

        while len(result)<k:
            result.append(list1.pop(0)[1])

        return result

        