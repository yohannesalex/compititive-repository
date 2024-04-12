# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        m, n = len(board), len(board[0])
        click_r, click_c = click
        visited = set()
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        def dfs(r, c):
            if board[r][c] != 'E':
                return

            mine = 0
            visited.add((r,c))
            for i , j in directions:
                new_row = r + i
                new_col = c + j
                if inbound(new_row,new_col) and board[new_row][new_col] == "M":
                    mine+=1
            if mine > 0:
                board[r][c] = str(mine)
            else:
                board[r][c] = 'B'
                for dr, dc in directions:
                    if inbound(r+dr,c+dc) and (r+dr,c+dc) not in visited:
                        dfs(r + dr, c + dc)

        if board[click_r][click_c] == 'M':
            board[click_r][click_c] = 'X'
        else:
            dfs(click_r, click_c)

        return board
