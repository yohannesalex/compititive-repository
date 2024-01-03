class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) < len(nums2):
            gre=nums2
            low=nums1
        else:
            gre=nums1
            low=nums2
        minLength=min(len(nums1),len(nums2))
        maxLength=max(len(nums1),len(nums2))
        pt1=0
        pt2=0
        while pt1 < maxLength and pt2 < minLength:
            if gre[pt1] == low[pt2]:
                return gre[pt1]
            elif gre[pt1] > low[pt2]:
                pt2+=1
            else:
                pt1+=1
        return -1