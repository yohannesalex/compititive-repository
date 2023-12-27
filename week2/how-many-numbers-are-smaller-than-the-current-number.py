class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count={}
        num=sorted(nums)
        res=[]
        l=len(nums)
        for i in range(len(num)):
            if num[i] not in count:
                count[num[i]] = i
        for j in nums:
            res.append(count[j])
        return res
        