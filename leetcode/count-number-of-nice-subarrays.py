class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        change=[0]*len(nums)
        for i in range (len(nums)):
            if nums[i]%2 == 0:
                change[i] = 0
            else:
                change[i] = 1
        count={0:1}
        pre=0
        ans=0
        for i in change:
            pre+=i
            if pre-k in count:
                ans+=count[pre-k]
            count[pre]=count.get(pre,0)+1
        return ans