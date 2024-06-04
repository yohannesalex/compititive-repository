# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        directions = [(1, 0),(0,1),(-1,0), (0,-1)]
        def inbound(row , col):
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
                return False
            return True
        seen = set()
        
        def dfs(i , j):
            nonlocal cur
            
            seen.add((i,j))
            cur+=grid[i][j]
            for row , col in directions:
                new_row = i + row
                new_col = j + col
                if inbound(new_row, new_col) and (new_row,new_col) not in seen and grid[new_row][new_col]!=0:
                    dfs(new_row, new_col)
            return cur


        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur = 0
                if (i, j) not in seen and grid[i][j] != 0:
                    maxi = max(maxi, dfs(i , j))
                
        return maxi