class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        totalSum=0
        for i in range(len(nums)):
            totalSum+=nums[i]
        beforesum=0
        results=[]
        n=len(nums)
        for i in range(len(nums)):
            results.append(totalSum+(2*i-n)*nums[i]-2*beforesum)
            beforesum=beforesum+nums[i]
        return results


        