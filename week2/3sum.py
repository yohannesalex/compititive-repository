class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        List=[]
        for i, a in enumerate (nums):
            if i > 0 and a==nums[i-1]:
                continue
            pt1=i+1
            pt2=len(nums)-1
            while pt2 > pt1:
                threesum=nums[pt1] + nums[pt2] + a
                if threesum > 0:
                    pt2-=1
                elif threesum < 0:
                    pt1+=1
                else:
                    List.append([a,nums[pt1],nums[pt2]])
                    pt1+=1
                    while nums[pt1]==nums[pt1-1] and pt2>pt1:
                        pt1+=1
           
        return List