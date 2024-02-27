class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        path=[]
        def comb(num):
            if len(path) == k:
                res.append(path.copy())
                return 
            for candi in range(num, n+1):
                path.append(candi)
                comb(candi+1)
                path.pop()
        comb(1)
        return res
