# Problem: Most Profit Assigning Work - https://leetcode.com/problems/most-profit-assigning-work/

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        comp = []
        for i in range(len(worker)):
            comp.append((profit[i], difficulty[i]))
        comp.sort(reverse = True)
        worker.sort(reverse = True)
        pt1 = 0
        pt2 = 0
        max_profit = 0
        while pt2 < len(worker) and pt1< len(worker):
            if worker[pt1] < comp[pt2][1]:
                pt2+=1
            else:
                max_profit+=comp[pt2][0]
                pt1+=1
        return max_profit
