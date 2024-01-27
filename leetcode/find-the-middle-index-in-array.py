class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pref=[]
        post=[]
        cur=0
        for i in range(len(nums)):
            cur+=nums[i]
            pref.append(cur)
        cur=0
        for j in range(len(nums)-1,-1,-1):
            cur+=nums[j]
            post.append(cur)
        l=0
        r=len(nums)-1
        while l < len(nums) and r >=0:
            if pref[l] == post[r]:
                return l
            l+=1
            r-=1
        return -1