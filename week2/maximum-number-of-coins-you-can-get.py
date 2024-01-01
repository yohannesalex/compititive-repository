class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n=len(piles)-2
        k=len(piles)//3
        res=0
        for i in range(k):
            res+=piles[n]
            n-=2
        return res
