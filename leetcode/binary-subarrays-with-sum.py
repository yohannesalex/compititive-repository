class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        d = {0:1}
        sums = 0
        ans = 0
        for i in range(len(nums)):
            sums += nums[i]
            if sums-goal in d:
                ans += d[sums-goal]
            d[sums] = d.get(sums, 0) + 1
        return ans