# Problem: Sum of Prefix Scores of Strings - https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        counter = defaultdict(int)
        for word in words:
            pre = ''
            for i in word:
                pre+=i
                counter[pre]+=1
        ans = []
        for word in words:
            pre = ''
            cur = 0
            for i in word:
                pre+=i
                if pre in counter:
                    cur+=counter[pre]
            ans.append(cur)
        return ans




