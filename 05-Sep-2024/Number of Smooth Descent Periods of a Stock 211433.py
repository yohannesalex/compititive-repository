# Problem: Number of Smooth Descent Periods of a Stock - https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        arr = []
        i = 0
        flag = False
        while i < len(prices) - 1:
            cur = 1
            while i < len(prices) - 1 and prices[i] - prices[i + 1] == 1:
                cur += 1
                i += 1
                flag = True
            if flag:
                flag = False
            else:
                cur = 1  
            arr.append(cur)
            i += 1
        
        if i == len(prices) - 1:
            arr.append(1)
        
        ans = 0
        
        def fac(num):
            return num * (num + 1) // 2
        
        for i in arr:
            ans += fac(i)
        
        return ans
