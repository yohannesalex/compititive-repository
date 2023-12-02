class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        count={}
        for i in range(len(order)):
            count[order[i]]=i
        for i in range(len(words)-1):
            k=min(len(words[i]),len(words[i+1]))
            print(min(words[i],words[i+1]))
            for j in range(k):
                if count.get(words[i][j] ) !=count.get(words[i+1][j]):
                    if count.get(words[i][j] ) > count.get(words[i+1][j]):
                        return False
                    break
               
            else:

                if len(words[i]) > len(words[i+1]):
                        return False
                    
        return True




