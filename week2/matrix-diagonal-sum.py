class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res=0
        l=len(mat)-1
        for i in range(len(mat)):
            res+=mat[i][i]
            res+=mat[i][l]
            l-=1
        if len(mat)%2==0:
            return res
        return res-mat[len(mat)//2][len(mat)//2]