# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        offset = 1
        res = [0]
        
        for i in range(1,n+1):
            if i & (i - 1) == 0:
                offset*=2
            res.append(1+res[i-offset])
        return res