# Problem: Maximal Score After Applying K Operations - https://leetcode.com/problems/maximal-score-after-applying-k-operations

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        heap = []
        for i in nums:
            heap.append(-i)
        heapify(heap)

        for i in range(k):
            cur = -heapq.heappop(heap)

            ans+= cur
            heapq.heappush(heap, -ceil(cur/3))
        return ans