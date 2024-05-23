# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root 
        for c in  word: 
            idx = ord(c) - 97
            if cur.children[idx] == None: 
                cur.children[idx] = TrieNode() 
            cur = cur.children[idx] 
        cur.is_end = True

    def search(self, word: str) -> bool:
        return self.s(word,self.root)
    
    def s(self, word,cur):
        for i,c in enumerate(word):
            idx = ord(c) - 97
            if c == ".":
                for child in cur.children:
                    if child:
                        if self.s(word[i+1:],child):
                            return True
                return False

            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        
        if cur.is_end: 
            return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)