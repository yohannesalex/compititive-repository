# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res=[]
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                l1 = set(words[i])
                l2 = set(words[j])
                if not l1.intersection(l2):
                    res.append(len(words[i]) * len(words[j]))
        
        if res:
            return max(res)
        return 0
