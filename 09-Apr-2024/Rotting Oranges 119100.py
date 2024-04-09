# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        direction = [[0,1], [1,0], [-1,0], [0,-1]]
        que = deque()
        fresh=0
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] == 2:
                    que.append([i,j])
        def inbound(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return False
            return True
        while que and fresh > 0:
            for i in range(len(que)):
                row,col = que.popleft()
                for r , c in direction:
                    new_row = row + r
                    new_col = col + c
                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        que.append([new_row, new_col])
                        fresh-=1
            time+=1
        if fresh:
            return -1
        return time


