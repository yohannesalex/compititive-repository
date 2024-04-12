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
                    # if inbound(new_row,new_col) and mat[new_row][new_col] == 0:
                    #     is_zero = True
                    if inbound(new_row,new_col) and (new_row, new_col) not in visited:
                        que.append((new_row, new_col))
                        visited.add((new_row,new_col))
            # if is_zero:
            #     return length
            length+=1
                

        
        
        return ans
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # visited = [[False for i in range(len(mat[0]))] for j in range(len(mat))]
        # # visited = set()
        # def inbound(row, col):
        #     return (0 <= row < len(mat) and 0 <= col < len(mat[0]))

        # que = deque()
        # for i in range(len(mat)):
        #     for j in range(len(mat[0])):
        #         if mat[i][j] == 0:
        #             que.append((i,j))
        #             visited[i][j] = True
        
        # level = 0
        # while que:
        #     n = len(que)
        #     for i in range(n):
        #         row , col = que.popleft()
        #         if mat[row][col] == 1:
        #             mat[row][col] = level
                
        #         for v , h in directions:
        #             new_row = row + h
        #             new_col = col + v
        #             if inbound(new_row,new_col) and not visited[new_row][new_col]:
        #                 visited[new_row][new_col] = True
        #                 que.append((new_row , new_col))
        #     level += 1
        # return mat
        # # if not mat or not mat[0]:
        # #     return []

        # # m, n = len(mat), len(mat[0])
        # # queue = deque()
        # # MAX_VALUE = m * n
        
        # # # Initialize the queue with all 0s and set cells with 1s to MAX_VALUE.
        # # for i in range(m):
        # #     for j in range(n):
        # #         if mat[i][j] == 0:
        # #             queue.append((i, j))
        # #         else:
        # #             mat[i][j] = MAX_VALUE
        
        # # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # # while queue:
        # #     row, col = queue.popleft()
        # #     for dr, dc in directions:
        # #         r, c = row + dr, col + dc
        # #         if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][col] + 1:
        # #             queue.append((r, c))
        # #             mat[r][c] = mat[row][col] + 1
        
        # # return mat