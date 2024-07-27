# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            c=''
            for j in str(nums[i]):
                c=c+str(mapping[int(j)])
            nums[i]=c
        nums.sort(key=lambda x:int(x))
        d={mapping[i]:str(i) for i in mapping}
        for i in range(len(nums)):
            c=''
            for j in str(nums[i]):
                c=c+d[int(j)]
            nums[i]=int(c)
        return nums