# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        compSet = []
        comMap = defaultdict(list)
        for i in range(len(pattern)):
            comMap[pattern[i]].append(i)
        for key ,val in comMap.items():
            compSet.append(val)
        compSet.sort()
        
        for word in words:
            cur = defaultdict(list)
            for i in range(len(word)):
                cur[word[i]].append(i)
            curList = []
            for key ,val in cur.items():
                curList.append(val)
            curList.sort()
            if curList == compSet:
                ans.append(word)
        return ans
