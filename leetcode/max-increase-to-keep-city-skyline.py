class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        res = []
        for i in range(len(grid)):
            val = []
            for j in range(len(grid[0])):
                val.append(0)
            res.append(val)
        
        for i in range(len(grid)):
            maxim = max(grid[i])
            for j in range(len(grid[i])):                
                res[i][j] = maxim
        for i in range(len(grid)):
            maxim = float("-inf")
            for j in range(len(grid[i])):
                maxim = max(maxim,grid[j][i])
            for j in range(len(grid[i])):
                res[j][i] = min(maxim,res[j][i])
        
        ans = 0
        for i in range(len(res)):
            for j in range(len(res[0])):
                ans += (res[i][j]-grid[i][j])
        return ans


