# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre = arr[0]
        ans = []
        preArr = [0,pre]
        for i in range(1, len(arr)):
            pre = pre ^ arr[i]
            preArr.append(pre)
        for q in queries:
            ans.append(preArr[q[1]+1] ^ preArr[q[0]])
        return ans
