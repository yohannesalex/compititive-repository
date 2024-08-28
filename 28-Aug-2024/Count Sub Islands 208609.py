# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(1,0), (0,1), (-1,0), (0, -1)]
        grid = set()
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                if grid1[i][j] == 1:
                    grid.add((i,j))
        def bounded(row , col):
            if 0 <= row < len(grid2) and 0<= col < len(grid2[0]):
                return True
            return False
        def checker(nums):
            for i in nums:
                if i not in grid:
                    return False
            return True
        visited = set()
        def dfs(i , nums):
            nums.append(i)
            visited.add(i)
            for r , c in directions:
                newRow = i[0] + r
                newCol = i[1] + c
                if bounded(newRow, newCol) and grid2[newRow][newCol] == 1 and (newRow, newCol) not in visited:
                    dfs((newRow, newCol), nums)
            return nums
        ans = 0
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i, j) not in visited  and grid2[i][j] == 1:
                    if checker(dfs((i,j), [])):
                        ans +=1
        return ans

        




