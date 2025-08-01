# 📌 Problem: Leetcode 119 – Pascal’s Triangle II
# Given an integer `rowIndex`, return the rowIndex-th (0-indexed) row of Pascal’s Triangle.
# In Pascal’s Triangle, each number is the sum of the two numbers directly above it.

# 🧠 Approach:
# - Initialize a result list that will store each row of the triangle.
# - Start from count = 0 and build rows one by one up to rowIndex.
# - For each row:
#   - Create a temporary list.
#   - First and last elements are always 1.
#   - For other elements, use the formula: current = previous_row[i-1] + previous_row[i].
# - Append each row to the result list.
# - After building up to the desired row, return result[rowIndex].

# 💬 Personal Note:
# This solution is part of my Python + Leetcode learning grind.
# Some logic (like list-based triangle building) may require tweaks for raw IDEs.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        count = 0
        temp_list = []
        result = []
        if rowIndex==0:
            return [1]

        while count!=rowIndex+1:
            temp_list=[]
            for i in range(0,count+1):
                if i==0 or i==count:
                    temp_list.append(1)
                else:
                    temp_list.append(result[-1][i]+result[-1][i-1])
            result.append(temp_list)
            count+=1
        return result[rowIndex]