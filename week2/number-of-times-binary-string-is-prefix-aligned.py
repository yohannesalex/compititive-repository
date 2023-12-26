class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count=0
        st=[0]*len(flips)
        res=0
        maxi=0
        for i in range(len(flips)):
            st[flips[i]-1] = 1
            count+=1
            maxi=max(maxi,flips[i])
            if maxi == count:
                res+=1
        return res
