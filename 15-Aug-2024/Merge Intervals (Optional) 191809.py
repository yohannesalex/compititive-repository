# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        p1 , p2 = 0 , 1
        while p2<= len(intervals)-1 and p1<=p2:
            last_of_p1_interval = intervals[p1][len(intervals[p1])-1]
            first_of_p2_interval = intervals[p2][0]
            first_of_p1_interval = intervals[p1][0]
            last_of_p2_interval = intervals[p2][len(intervals[p2])-1]
            if first_of_p2_interval <= last_of_p1_interval:
                intervals[p1][0] = min(first_of_p1_interval,first_of_p2_interval)
                intervals[p1][len(intervals[p1])-1] = max(last_of_p1_interval,last_of_p2_interval)
                temp=p2
                intervals.remove(intervals[temp])
            else:
                p1+=1
                p2+=1
                continue
        return intervals