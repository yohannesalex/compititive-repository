# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions = [[1,1],[0,1],[1,0],[0,-1],[-1,0],[-1,1],[-1,-1],[1,-1]]
        def inbound(row,col):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return False
            return True

        que=deque()
        visited=set()
        que.append([0,0,1])
        if grid[0][0] == 1:
            return -1
        visited.add((0,0))
        while que:
            
            r , c, length = que.popleft()
            if [r,c] == [len(grid)-1,len(grid[0])-1]:
                return length
            if grid[r][c] !=0:
                continue
            for i,j in directions:
                new_row = r + i
                new_col = c + j
                if inbound(new_row,new_col) and grid[new_row][new_col] == 0 and (new_row,new_col) not in visited:
                    que.append([new_row,new_col, length+1])
                    visited.add((new_row,new_col))
            
        return -1
