# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i]*=-1
        heapify(piles)
        for i in range(k):
            cur = heapq.heappop(piles)
            cur = cur//2
            heapq.heappush(piles,cur)
        
        return -1*(sum(piles))
            

           
    