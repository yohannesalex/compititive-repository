class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count={0:0,1:0}
        l=0
        res=0
        for r in range(len(nums)):
            count[nums[r]]+=1
            if (r-l+1) -(count.get(1))<=1:
                res=max(res,r-l+1)
            else:
                count[nums[l]]-=1
                l+=1
        return res-1