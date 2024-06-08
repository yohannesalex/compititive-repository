# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        cur1 = ""
        cur2 = ""
        for i in word1:
            cur1+=i
        for i in word2:
            cur2+=i
        return cur1 == cur2
        