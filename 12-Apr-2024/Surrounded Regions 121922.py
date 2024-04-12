# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        direction=[[1,0],[0,1],[-1,0],[0,-1]]
        def inbound(row , col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            return True
        def dfs(r,c):
           
            if not inbound(r, c) or board[r][c] != "O":
                return
            board[r][c] = "Y"
            for i , j in direction:
                new_r = r + i
                new_c = c + j
                dfs(new_r, new_c)
        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r in [0,len(board)-1] or c in [0,len(board[0])-1]) and board[r][c] == "O":
                    dfs(r,c)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "Y":
                    board[i][j] = "O"
        


        