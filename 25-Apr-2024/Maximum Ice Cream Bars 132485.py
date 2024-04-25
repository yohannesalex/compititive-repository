# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = [0] *(max(costs)+1)
        for i in costs:
            count[i]+=1
        res = 0
        print(count)
        i = 1
        while i < len(count):
            while count[i]> 0 and coins > 0:
                if i <= coins:
                    count[i]-=1
                    coins-=i
                    res+=1
                else:
                    break
            i+=1
            
        return res