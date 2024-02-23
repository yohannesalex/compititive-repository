class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def mod_pow(num, _pow, mod):
            if _pow <= 1:
                return num**_pow
            if _pow % 2:
                return ((mod_pow(num,_pow-1,mod))*num) % mod
            else:
                return ((mod_pow(num,_pow//2,mod))**2) % mod

        return (mod_pow(5,ceil(n/2),10**9 + 7) * mod_pow(4,n//2,10**9 + 7)) % (10**9 + 7)
        