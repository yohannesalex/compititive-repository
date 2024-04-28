# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        path=set()
        row = len(board)
        col = len(board[0])
        def dfs(r,c,idx):
            if idx == len(word):
                return True
            if r < 0 or r>=row or c < 0 or c >=col or word[idx] != board[r][c] or (r,c) in path:
                return False
            path.add((r,c))
            res = dfs(r+1, c , idx+1) or dfs(r, c+1 , idx+1) or dfs(r-1, c , idx+1) or dfs(r, c-1 , idx+1) 
            path.remove((r,c))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False