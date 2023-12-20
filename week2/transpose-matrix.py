class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res=[]
        k=len(matrix[0])
        for i in range(k):
            cur=[]
            for j in range(len(matrix)):
                cur.append(matrix[j][i])
            res.append(cur)
          
        return res
