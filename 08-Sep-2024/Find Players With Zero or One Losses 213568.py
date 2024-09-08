# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win=[]
        loss=[]
        count={}
        countloss={}
        for i in matches:
            count[i[0]] = 1+ count.get(i[0],0)
        for n in matches:
            if n[1] in count:
                del count[n[1]]
        for i in count:
            win.append(i)
        for j in matches:
            countloss[j[1]] = 1 + countloss.get(j[1],0)
        for k in  countloss:
            if countloss.get(k) == 1:
                loss.append(k)
        win.sort()
        loss.sort()
        return [win,loss]