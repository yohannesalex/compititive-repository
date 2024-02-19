class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        # left=0
        # l=[]
        # cur = nums[0]
        # maxim = float("-inf")
        # i=1
        # while i < len(nums):
        #     while i < len(nums) and nums[i] > nums[i-1]:
        #         cur+=nums[i]
        #         i+=1
        #     else:
                
        #         l.append(ceil(cur/(i-left)))
        #         left=i
        #         if i < len(nums):
        #             cur=nums[i]
        #         i+=1
        # k=[]
        # if nums[len(nums)-1]  <= nums[len(nums)-2]:
        #     k.append(nums[len(nums)-1] )
        # elif nums[0] >= nums[1]:
        #     k.append(nums[0])
        # else:
        #     for i in range(1,len(nums)-1):
        #         if nums[i] <= nums[i-1] and nums[i] >= nums[i+1]:
        #             k.append(nums[i])
        # print(l,k)

        # n=sum(l)
        # if k:
        #     a=max(k)
        #     return max(ceil(n/len(l)),a)
        # else:
        #     return ceil(n/len(l))

        maxi = float("-inf")
        pre=0
        
        for i in range(len(nums)):
            pre+=nums[i]
            maxi = max(maxi, ceil(pre/(i+1)))
            
        return maxi