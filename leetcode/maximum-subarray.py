class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        run =0

        for i in nums:
            
            
            if run < 0:
                run=0
            
            run+=i
            
            maxi=max(run,maxi)
        return maxi