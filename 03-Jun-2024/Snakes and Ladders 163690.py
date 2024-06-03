# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        arr = []
        n , m = len(board) , len(board[0])
        size = n * m
        directions = [(0,1) , (0,-1)]
        visited = set([1])
        def inbound(row, col):
            return (0 <= row < len(board) and 0 <= col < len(board[0]))
        dire = 0
        i , j = len(board) - 1 , 0
        k = 0
        while k < size:
            if inbound(i , j):
                arr.append(board[i][j])
                i += directions[dire][0]
                j += directions[dire][1]
            else:
                i += ((-1) * directions[dire][0])
                j += ((-1) * directions[dire][1])

                dire = 1 - dire

                i -= 1 
               
                arr.append(board[i][j])
               
                i += directions[dire][0]
                j += directions[dire][1]
            k += 1
        
        que = deque()
        que.append(1)

        s = len(board)
        level = 0
        while que:
            n = len(que)
            for i in range(n):
                idx = que.popleft()
                if idx == (s ** 2):
                    return level
    
                for i in range(6):
                    newidx = idx + i + 1
                    if  newidx <= (s**2) and arr[newidx - 1] != -1:
                        if arr[newidx - 1] <= (s**2) and arr[newidx - 1] not in visited:
                            visited.add(arr[newidx - 1])
                            que.append(arr[newidx - 1])
                    else:
                        if newidx <= (s**2) and newidx not in visited:
                            visited.add(newidx)
                            que.append(newidx)
            level += 1
        return -1




























