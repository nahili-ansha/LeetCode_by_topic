# https://leetcode.com/problems/max-area-of-island/

# Max Area of Island

from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        seen = set()
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        maxArea = 0 

        def isValid(row, column):
            return 0 <= row < m and 0 <= column < n and grid[row][column] == 1

        def dfs(row, column):
            area = 1
            for dx, dy in directions:
                new_row, new_column = row + dx, column + dy
                if isValid(new_row, new_column) and (new_row, new_column) not in seen:
                    seen.add((new_row, new_column))
                    area += dfs(new_row, new_column)
            return area

        for row in range(m):
            for column in range(n):
                if (row,column) not in seen and grid[row][column] == 1:
                    seen.add((row, column))
                    maxArea = max(maxArea, dfs(row, column))
        return maxArea
    
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0