# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def inbound(r,c):
            if r == len(matrix) or c == len(matrix[0]) or r < 0 or c < 0:
                return False
            return True
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                mini = float("inf")
                if inbound(i+1,j+1):
                    mini = min(mini,matrix[i+1][j+1])
                if inbound(i+1,j-1):
                    mini = min(mini,matrix[i+1][j-1])
                if inbound(i+1,j):
                    mini = min(mini,matrix[i+1][j])
                if mini != float("inf"):
                    matrix[i][j]+=mini
        mini = float("inf")
        for i in matrix[0]:
            mini= min(mini,i)
        return mini