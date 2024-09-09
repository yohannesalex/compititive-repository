# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n+1):
            offset = 0
            cur = 0
            while i >= 2**offset:
                if i & 2**offset:
                    cur+=1
                offset+=1
            ans.append(cur)
        return ans
