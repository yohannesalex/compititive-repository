class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      
        count={0:1}
        res=0
        pre=0
        for i in nums:
            pre+=i
            if pre-k in count:
                res+=count.get(pre-k)
                
            count[pre]=1+count.get(pre,0)
        return res
        