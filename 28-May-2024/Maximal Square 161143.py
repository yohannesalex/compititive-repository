# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        cur = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        maxi = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        cur[i][j] = 1
                    else:
                        cur[i][j] = min(cur[i-1][j], cur[i][j-1], cur[i-1][j-1]) + 1
                    maxi = max(maxi, cur[i][j])
        
        return maxi ** 2
