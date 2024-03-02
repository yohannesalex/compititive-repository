class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
       res=[]
       for i,j in zip(weights,weights[1:]):
           res.append(i+j)
       res.sort()
       mini=sum(res[:k-1])
       maxi=sum(res[len(res)-k+1:])
       return maxi-mini