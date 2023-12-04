class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res=0
        maxi=0
        for i in nums:
            if i == 1:
                res+=1
                maxi=max(res,maxi)
            else:
                res=0
        return maxi
            
