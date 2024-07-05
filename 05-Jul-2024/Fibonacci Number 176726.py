# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        pre = 0
        pre2 = 1
        if n <=1:
            return n
        for i in range(2,n+1):
            cur = pre+pre2
            pre=pre2
            pre2=cur
        return pre2