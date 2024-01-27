class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res=[]
        k=0
        for i in nums:
            k+=i
            res.append(k)
        return res
