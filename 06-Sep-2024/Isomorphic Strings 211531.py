# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        countS = defaultdict(list)
        countT = defaultdict(list)
        for i in range(len(s)):
            countS[s[i]].append(i)
        for i in range(len(s)):
            countT[t[i]].append(i)
        setS = []
        setT = set()
        for key , val in countS.items():
            setS.append(val)
        for key , val in countT.items():
            if val not in setS:
                return False
        return True
            

        