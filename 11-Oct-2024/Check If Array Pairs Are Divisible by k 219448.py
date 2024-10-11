# Problem: Check If Array Pairs Are Divisible by k - https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/

class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count=defaultdict(int)
        res=0
        for i in arr:
            if count[(-i)%k] >=1:
                count[(-i)%k]-=1
                res+=1
            else:
                count[i%k]+=1
        return res == len(arr)//2