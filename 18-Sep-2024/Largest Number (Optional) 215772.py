# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs=[]
        for i in nums:
            strs.append(str(i))
        for i in range(len(strs)-1):
            for j in range (len(strs)-1):
                if int(str(strs[j])+ str(strs[j+1])) < int(str(strs[j+1])+str(strs[j])):
                    strs[j] , strs[j+1] = strs[j+1] , strs[j]
        if strs[0] == "0":
            return "0"
        return "".join(strs)