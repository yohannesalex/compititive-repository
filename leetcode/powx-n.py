class Solution:
    def myPow(self, x: float, n: int) -> float:
        real = n
        if n == 0:
            return 1
        def power(num,p):
            if p <= 1:
                return num * p
            temp= power(num,p//2)
            if p %2==0:

                return temp * temp
            else:
                return temp * temp *x
        ans = power(x,abs(n))
        if real < 0:
            return 1/ans
        return ans
