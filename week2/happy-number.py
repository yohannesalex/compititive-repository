class Solution:
    def isHappy(self, n: int) -> bool:
   
        for i in range(30):
            m=str(n)
            k=0
            for i in m:
                k+=int(i)**2
            if k==4:
                return False
            n=k
           
        return True
