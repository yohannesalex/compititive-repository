# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo ={}
        def dp(row , col):
            if row== 0 or col == 0:
                return 1
            
            if (row, col) not in memo:
                memo[(row, col)] = dp(row, col-1) + dp(row-1, col)
            return memo[(row,col)]
        return dp(m-1, n-1)
            
