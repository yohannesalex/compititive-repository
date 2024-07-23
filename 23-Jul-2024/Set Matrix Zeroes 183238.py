# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cur = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                cur[i][j] = matrix[i][j]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if cur[i][j] == 0:
                    for k in range(len(matrix)):
                        matrix[k][j] = 0
                    for l in range(len(matrix[0])):
                        matrix[i][l] = 0
        print(cur)
        
                    