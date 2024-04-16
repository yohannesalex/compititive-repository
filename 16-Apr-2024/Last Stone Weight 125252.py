# Problem: Last Stone Weight - https://leetcode.com/problems/last-stone-weight/

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        
        heapify(stones)
        while stones and len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if x<y:
                heapq.heappush(stones,-(y-x))
        if stones:
            return -stones[0]
        return 0
