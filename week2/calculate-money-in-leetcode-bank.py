class Solution:
    def totalMoney(self, n: int) -> int:
        k=1
        l=1
        res=0
        m=1
        while l<=n:
            if (l-1)>=7 and (l-1)%7==0:
                m+=1
                k=m
            res+=k
            k+=1
            l+=1
        return res
        # k = 0
        # l = 1
        # money = 0
        # while l < n+1:
        #     money += (l%7)+k
        #     if l>=7 and l%7==0:
        #         k+=1
        #     l += 1
        # return money


        