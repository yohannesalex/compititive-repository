# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pre=[]
        pr=0
        for i in nums:
            pr+=i
            pre.append(pr)
        post=[]
        po=0
        for i in range(len(nums)-1,-1,-1):
            po+=nums[i]
            post.append(po)
        post.reverse()
        pt1=0
        while pt1<len(nums):
            if post[pt1] == pre[pt1]:
                return pt1

            pt1+=1
        return -1

        