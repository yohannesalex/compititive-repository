class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        count={}
        countl=[]
        nums.sort(reverse = True)
        res=0
        
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for i in count:
           countl.append([i,count[i]])
        for i in range(len(countl)):
            res+=countl[i][1] * (len(countl)-i-1)
        return res