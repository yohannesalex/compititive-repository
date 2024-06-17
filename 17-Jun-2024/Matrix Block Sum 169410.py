# Problem: Matrix Block Sum - https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, ma: List[List[int]], k: int) -> List[List[int]]:
        n = len(ma)
        m = len(ma[0])
        def isval(x,y):
            if x<0 or y<0 or x>=n or y>=m:
                return False
            return True
        t = [[0 for i in range(m)]for j in range(n)]
        for i in range(min(n,k+1)):
            for j in range(min(k+1,m)):
                t[0][0] += ma[i][j]
        for i in range(n):
            for j in range(m):
                if i != 0:
                    t[i][j] = t[i-1][j]
                    if isval(i-k-1,j):
                        for v in range(-1*k,k+1):
                            if isval(i-k-1,j+v):
                                t[i][j] -= ma[i-k-1][j+v]
                    if isval(i+k,j):
                        for v in range(-1*k,k+1):
                            if isval(i+k,j+v):
                                t[i][j] += ma[i+k][j+v]
                else:
                    if j!=0:
                        t[i][j] = t[i][j-1]
                        if isval(i,j-k-1):
                            for v in range(-1*k,k+1):
                                if isval(i+v,j-k-1):
                                    t[i][j] -= ma[i+v][j-k-1]
                        if isval(i,j+k):
                            for v in range(-1*k,k+1):
                                if isval(i+v,j+k):
                                    t[i][j] += ma[i+v][j+k]
        return t