# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        visible = sum(rolls)
        totalObservation = len(rolls) + n
        nonVisible = (totalObservation * mean) - visible
        print(nonVisible)
        if  nonVisible < n or nonVisible > n * 6 :
            return []
        else:
            ans = []
            for i in range(n):
                ans.append(nonVisible//n)
            cur =nonVisible - sum(ans)
            for i in range(cur):
                ans[i]+=1
            return ans
