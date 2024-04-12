# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        def inbound(row,col):
            if row < 0 or row >= len(mat) or col < 0 or len(mat[0]) <= col:
                return False
            return True
        ans=[[0]*len(mat[0]) for i in range(len(mat))]
        que = deque()
        visited = set()
        length = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    que.append((i,j))
                    visited.add((i,j))
        while que:
            k = len(que)
            for i in range(k):
                r,c = que.popleft()
                if mat[r][c] == 1:
                    ans[r][c] = length
                for i , j in directions:
                    new_row = r + i
                    new_col = c + j
                    
                    if inbound(new_row,new_col) and (new_row, new_col) not in visited:
                        que.append((new_row, new_col))
                        visited.add((new_row,new_col))
           
            length+=1
        return ans
