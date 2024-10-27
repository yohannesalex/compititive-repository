# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        heap = []
        ans = 0
        for i in nums:
            heapq.heappush(heap,-i)
        for i in range(k):
            cur = -heapq.heappop(heap)
            ans+= cur
            heapq.heappush(heap,-(cur+1))
        return ans
