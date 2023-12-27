class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        count=defaultdict()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j not in count:
                    count[i+j]=[mat[i][j]]
                else:
                    count[i+j].append(mat[i][j])
        res=[]
        for i in count:
            if i %2 !=0:
                res.extend(count[i])
            else:
                res.extend(count[i][::-1])
        return res