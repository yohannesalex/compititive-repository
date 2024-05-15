# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo ={}
        pass_=[1,7,30]
        def dfs(i):
            if i == len(days):
                return 0
            if i in memo:
                return memo[i]
            choose = float("inf")
            for j in range(len(costs)):
                cur = i
                while cur < len(days) and days[cur] < days[i] + pass_[j]:
                    cur+=1
                choose = min(choose, costs[j]+dfs(cur))
                memo[i] = choose
            return memo[i]
        return dfs(0)


                