# Problem: Minimum Time Difference - https://leetcode.com/problems/minimum-time-difference/

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        cur = []
        for i in timePoints:
            k = i.split(':')
            cur.append(int(k[0])*60+ int(k[1]))
        cur.sort()
        mini = float("inf")
        for i in range(len(cur)-1):
            mini = min(cur[i+1] - cur[i], mini)
        mini = min(1440 -cur[i+1] + cur[0], mini)
        return mini