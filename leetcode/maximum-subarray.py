class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = float(-inf)
        run = float(-inf)
        for i in range(len(nums)):
            value = run + nums[i]
            run = max(nums[i] , value)
            maxi = max(maxi , run)
        return maxi 