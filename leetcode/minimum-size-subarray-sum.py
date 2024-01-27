class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=float("inf")
        l=0
        r=0
        sumi=0
        while r < len(nums):
            sumi+=nums[r]
            while sumi >= target:
                mini=min(mini,r-l+1)
                sumi-=nums[l]
                l+=1
            r+=1
        if mini == float("inf"):
            return 0
        return mini
