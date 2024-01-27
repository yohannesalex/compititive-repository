class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        count={1:0  , 0:0}
        maxi=0
        while r < len(nums):
            count[nums[r]] = 1 + count.get(nums[r],0)
            if count[0] > k:
                count[nums[l]]-=1
                l+=1
            maxi=max(maxi,r-l+1)
            r+=1
        
        return maxi
            
            
