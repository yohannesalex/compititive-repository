
# def isBadVersion(version: int) -> bool:
    
class Solution:
    def firstBadVersion(self, n: int) -> int:
        self.mid = n//2
        def binary(l,r):
            if isBadVersion(self.mid) == True and isBadVersion(self.mid-1) == False:
                return self.mid
            elif isBadVersion(self.mid) == True:
                r = self.mid-1
            elif isBadVersion(self.mid) == False:
                l = self.mid+1
            self.mid = (l+r)//2
            return binary(l,r)
        return binary(1,n)

