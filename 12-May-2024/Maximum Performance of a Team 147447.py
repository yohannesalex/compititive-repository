# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        nums = list(zip(efficiency , speed))
        nums.sort(reverse=True)
        mod = 10 ** 9 + 7
        heap = []

       
        sumi = 0
        maxi = 0
        
        for i in range(len(nums)):
            heappush(heap , nums[i][1])
            sumi += nums[i][1]
            if len(heap) > k:
                cur = heappop(heap)
                sumi -= cur
            maxi = max(maxi , sumi * nums[i][0])
        return maxi % mod



