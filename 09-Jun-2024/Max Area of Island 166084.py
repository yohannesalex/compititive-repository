# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0),(0,1),(0,-1)]
        seen = set()
        def inbound(row, col):
            if row < 0 or col < 0 or col == len(grid[0]) or row == len(grid):
                return False
            return True
        def dfs(i, j):
            seen.add((i,j))
            area = 1
            for r , c in directions:
                newrow = r + i
                newcol = c + j
                if inbound(newrow,newcol) and grid[newrow][newcol] == 1 and  (newrow, newcol) not in seen:
                    area += dfs(newrow, newcol)
            return area
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in seen and grid[i][j] == 1:
                    ans = max(ans, dfs(i,j))
        return ans