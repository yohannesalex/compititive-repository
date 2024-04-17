# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        heap = []
        for i in freq.keys():
             
            heappush(heap, (-freq[i], i))
        ans = []
        for i in range(k):
            ans.append(heappop(heap)[1])
        return ans