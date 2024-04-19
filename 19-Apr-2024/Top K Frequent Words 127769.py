# Problem: Top K Frequent Words - https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count= Counter(words)
        cur = []
        for key, value in count.items():
            cur.append((-value, key))
        heapify(cur)
        
        res=[]
        for i in range(k):

            res.append(heapq.heappop(cur)[1])
        return res

        

        
            


