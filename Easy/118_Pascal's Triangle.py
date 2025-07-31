# 📌 Problem: Leetcode 118 – Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's Triangle.
# Each number is the sum of the two numbers directly above it in the previous row.

# 🧠 Approach:
# - Start with an empty result list and a row counter.
# - For each row:
#   - Initialize an empty temporary list.
#   - If it's the first or last index in the row, append 1.
#   - For other positions, calculate the value as the sum of the two numbers above it from the previous row.
# - After building each row, append it to the result.
# - Return the final result list after all rows are built.

# 💬 Personal Note:
# This code is part of my Python grind + Leetcode journey.
# Some Leetcode-only functions/structures may not work directly in a normal IDE without modification.

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        count = 0
        temp_list = []
        result = []
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]

        while count!=numRows:
            temp_list=[]
            for i in range(0,count+1):
                if i==0 or i==count:
                    temp_list.append(1)
                else:
                    temp_list.append(result[-1][i]+result[-1][i-1])
            result.append(temp_list)
            count+=1
        return result