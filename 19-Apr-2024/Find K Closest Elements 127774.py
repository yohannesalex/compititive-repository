# Problem: Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        res=[]
        cur = []
        for i in arr:
            cur.append((abs(i-x),i))
        heapify(cur)
        for i in range(k):
            res.append(heapq.heappop(cur)[1])
        return sorted(res)