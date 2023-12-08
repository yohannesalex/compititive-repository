class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n=len(nums)
        k=[]
        for i in range(0,n+1):
            k.append(i)
        for i in range(len(k)):
            if k[i] in nums:
                pass
            else:
                return k[i]