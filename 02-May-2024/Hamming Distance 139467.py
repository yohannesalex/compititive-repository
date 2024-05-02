# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x =format(x, '064b')
        y = format(y, '064b')
        ans = 0
        print(x,y)
        for i in range(min(len(x), len(y))-1,-1,-1):
            if x[i]!= y[i]:
                ans+=1
        ans+= abs(len(x)- len(y))
        return ans
