# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList == [] or secondList == []:
            return []


        res = []
        i = 0
        j = 0

        while i < len(firstList) and j < len(secondList):
            l = max(firstList[i][0], secondList[j][0])
            r = min(firstList[i][1], secondList[j][1])

            if l <= r :


                res.append([l, r])

            if firstList[i][1] < secondList[j][1]:
                i += 1


            else:
                j += 1        



        return res