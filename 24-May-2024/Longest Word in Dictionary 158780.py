# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/


class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def longestWord(self, words: List[str]) -> str:
        def insert(word):
            cur = self.root
            for i in word:
                idx = ord(i) - 97
                if cur.children[idx] == None:
                    cur.children[idx] = TrieNode()
                cur = cur.children[idx]
            cur.is_end = True
        
        seen = set()
        for i in words:
            seen.add(i)
        seen.add("")

        def search(word, st):
            cur = self.root
            for c in word:
                idx = ord(c) - 97
                if cur.children[idx] == None or st + c not in seen:
                    return (len(st), word)
                st += c
                cur = cur.children[idx]
            return (len(st), word)
                
        for word in words:
            insert(word)
        
        ans = []
        for word in words:
            ans.append(search(word, ""))
        
        ans.sort()
        maxi = ans[-1][0]
        if maxi == 0:
            return ""
        
        for i in range(len(ans)):
            if ans[i][0] == maxi:
                return ans[i][1]
