class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num=set(nums)
        
        maxi=0
        for i in nums:
            if i-1 in num:
                continue
            k=1
            while i+k in num:
                k+=1
            maxi=max(maxi,k)
        return maxi
