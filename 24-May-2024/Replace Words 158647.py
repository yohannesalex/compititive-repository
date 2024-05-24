# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]
class Solution:
    def __init__(self):
        self.root = TrieNode()
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        def insert(word):
            cur = self.root
            for i in word:
                idx = ord(i) - 97
                if cur.children[idx] == None:
                    cur.children[idx] = TrieNode()
                cur = cur.children[idx]
            cur.is_end = True
                   
        for word in dictionary:
            insert(word)
        ans = ""
        dic = set()
        for i in dictionary:
            dic.add(i)

        def search(word , st):
            cur = self.root
            for c in word:
                idx = ord(c) - 97
                if not cur.children[idx] or st in dic:
                    return st
                st+=chr(idx + 97)
                cur = cur.children[idx]
            
            
            return st
        for word in sentence.split(" "):
            temp = search(word,"")
            if temp == "" or temp not in dic:
                ans += word + " "
            else:
                ans +=temp+" "
        return ans[:len(ans)-1]
        
        


