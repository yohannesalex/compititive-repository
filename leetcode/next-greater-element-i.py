class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=0
        r=1
        res=[]
        while l < len(nums2)-1:
            while l < len(nums2)-1 and nums2[l] >= nums2[r]:
                r+=1
                if r == len(nums2):
                    res.append(-1)
                    l+=1
                    r=l+1
            if l < len(nums2)-1 and nums2[l] < nums2[r]:
                res.append(nums2[r])
                l+=1
                r=l+1
        res.append(-1)
        count={}
        for i in range(len(nums2)):
            count[nums2[i]] = res[i]
        ans=[]
        for i in nums1:
            ans.append(count[i])
        return ans

            
           
