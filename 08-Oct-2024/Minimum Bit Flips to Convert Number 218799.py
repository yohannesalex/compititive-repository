# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        maxi = max(start , goal)
        i = 0
        ans = 0
        while maxi >= 2**i:
            if start & 2**i != goal & 2**i:
                ans+=1
            i+=1
        return ans

