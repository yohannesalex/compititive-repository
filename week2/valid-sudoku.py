class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=len(board)
        cols=len(board[0])
        def dup(arr):
            se=set()
            for i in arr:
                if i!=".":
                    if i in se:
                        return False
                    else:
                        se.add(i)
            return True
        for i in range(rows):
            if not dup(board[i]):
                return False

      
        transpose_board=[[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                transpose_board[j][i] = board[i][j]

        for i in range(len(transpose_board)):
            if not dup(transpose_board[i]):
                return False
        blocks = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                blocks.append(board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3])

        r=len(blocks)
        c=len(blocks[0])

        for i in range(r):
            if not dup(blocks[i]):
                return False

        return True
            



        

        