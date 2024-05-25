# Problem: Number of Matching Subsequences - https://leetcode.com/problems/number-of-matching-subsequences/

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        look = defaultdict(list)
        for i , c in enumerate(s):
            look[c].append(i)
        for word in words:
            prev = -1
            Found = True
            for w in word:
                if not look[w]:
                    Found = False
                    break
                idx = bisect_left(look[w],prev)
                if idx == len(look[w]):
                    Found = False
                    break
                
                prev = look[w][idx]+1
            if Found:
                ans+=1
        return ans

