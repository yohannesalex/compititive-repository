# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        count = {}
        cur = []
        seen = set()
        for i in range(len(s1)):
            temp = set()
            S1 = s1[i]
            S2 = s2[i]
            
            for i in range(len(cur)):
                if S1 in cur[i] or S2 in cur[i]:
                    cur[i].add(S2) 
                    cur[i].add(S1)
                    seen.add(S2)
                    seen.add(S1)
                    break
                
            if S1 not in seen and S2 not in seen:
                temp.add(S1)
                temp.add(S2)
                cur.append(temp.copy())
                seen.add(S1)
                seen.add(S2)
        for i in range(len(cur)):
            for j in range(1 , len(cur)):
                if cur[i].intersection(cur[j]):
                    cur[i] = cur[i].union(cur[j])
        for i in seen:
            count[i] = i
        for i in cur:
            mini = min(i)
            for j in i:
                if count[j] > mini:
                    count[j] = mini
        ans = ""
        
        for i in baseStr:
            if i not in count:
                ans+=i
            elif i > count[i]:
                ans+=count[i]
            else:
                ans+=i
        return ans
        
                
