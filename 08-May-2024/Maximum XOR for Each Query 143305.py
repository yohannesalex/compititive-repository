# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        pre = []
        res=[]
        for i in range(len(nums)):
            if i == 0:
                pre.append(nums[i])
            else:
                pre.append(pre[-1] ^ nums[i])
        for i in range(len(pre)-1,-1,-1):
            cur = 0
            for j in range(maximumBit):
                if not pre[i] & 1<< j:
                    cur|= 1<< j
            res.append(cur)
        return res
