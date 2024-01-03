class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=0
        
        pt=len(nums)-1
        for i in range(len(nums)):
            while i < pt  :                
                if nums[i] + nums[pt] < target:
                    res+=(pt-i)
                    break
                else:
                    pt-=1
                    
            
        return res
