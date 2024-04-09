# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def isValid(rad):
            h = 0
            i = 0
            while(i < len(houses)):
                if(abs(houses[i] - heaters[h]) <= rad):
                    i += 1
                else:
                    h += 1
                if(h == len(heaters)):
                    return 0
            return 1
        houses.sort()
        heaters.sort()
        i, j = 0, 1000000000
        ans = 0
        while(i <= j):
            mid = (i+j)//2
            if(isValid(mid)):
                j = mid-1
                ans = mid
            else:
                i = mid+1
        return ans