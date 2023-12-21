class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maxi=-inf
        for i in range(1,len(grid)-1):
            for j in range(1,len(grid[0])-1):
                sumi=grid[i][j]+grid[i-1][j-1]+grid[i-1][j]+grid[i-1][j+1]+grid[i+1][j-1]+grid[i+1][j]+grid[i+1][j+1]
                maxi=max(sumi,maxi)
        return maxi