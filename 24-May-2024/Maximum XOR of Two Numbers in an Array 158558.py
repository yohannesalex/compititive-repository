# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(2) ]
class Solution:
    
    def __init__(self):
        self.root = TrieNode()
    
    def findMaximumXOR(self, nums: List[int]) -> int:

        def insert(num):
            cur = self.root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if not cur.children[bit]:
                    cur.children[bit] = TrieNode()
                cur = cur.children[bit]
        for i in nums:
            insert(i)
        maxi = 0
        for num in nums:
            cur = self.root
            value = 0
            for i in range(31, -1 , -1):
                bit = (num >> i) & 1
                opposite_bit = 1 - bit
                if cur.children[opposite_bit]:
                    value |= (1 << i)
                    cur = cur.children[opposite_bit]
                else:
                    cur = cur.children[bit]
            maxi = max(maxi,value)
        return maxi


                



