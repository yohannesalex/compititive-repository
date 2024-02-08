class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        nSet=len(set(nums))
        r=0
        k=set()
        res=0
        
        for i in range(len(nums)):
            k=set()
            for j in range(i,len(nums)):
                k.add(nums[j])
                if len(k)==nSet:
                    res+=1
        return res


        